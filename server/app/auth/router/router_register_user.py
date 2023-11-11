from pydantic import Field
from typing import Any

from fastapi import Depends, HTTPException, status

from app.utils import AppModel

from ..service import Service, get_service
from . import router


class RegisterUserRequest(AppModel):
    email: str
    password: str
    name: str
    surname: str
    center: str
    role: str


class RegisterUserResponse(AppModel):
    id: Any = Field(alias="_id")
    email: str
    name: str
    surname: str
    center: str
    role: str
    access_token: str


@router.post(
    "/users", status_code=status.HTTP_201_CREATED, response_model=RegisterUserResponse
)
def register_user(
        input: RegisterUserRequest,
        svc: Service = Depends(get_service),
) -> RegisterUserResponse:
    if svc.authRepository.get_user_by_email(input.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email is already taken.",
        )

    input = input.dict()
    user = svc.authRepository.create_user(input)

    if input["role"] == "specialist":
        svc.specialistRepository.create_specialist({"user_id": user["_id"], "center": input["center"]})
    if input["role"] == "parent":
        svc.parentRepository.create_parent({"user_id": user["_id"], "center": input["center"]})

    input["id"] = user["_id"]
    input["access_token"] = svc.jwt_svc.create_access_token(user=user)
    del input["password"]

    return RegisterUserResponse(**input)
