from typing import Any, List, Union

from fastapi import Depends
from pydantic import Field

from app.utils import AppModel
from .errors import InvalidCredentialsException

from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from .dependencies import parse_jwt_user_data


class SpecialistResponse(AppModel):
    id: Any = Field(alias="_id")
    school: str
    children: List[str]


class ParentResponse(AppModel):
    id: Any = Field(alias="_id")
    center: str
    children: List[str]


class GetMyAccountResponse(AppModel):
    id: Any = Field(alias="_id")
    email: str
    name: str
    surname: str
    role: str
    role_info: Union[SpecialistResponse, ParentResponse]


@router.get("/users/me", response_model=GetMyAccountResponse)
def get_my_account(
        jwt_data: JWTData = Depends(parse_jwt_user_data),
        svc: Service = Depends(get_service),
) -> dict[str, dict]:
    user = svc.authRepository.get_user_by_id(jwt_data.user_id)

    if not user:
        raise InvalidCredentialsException

    if user["role"] == "specialist":
        user['role_info'] = svc.specialistRepository.get_specialist_by_user_id(user_id=user['_id'])
    if user["role"] == "parent":
        user['role_info'] = svc.parentRepository.get_parent_by_user_id(user_id=user['_id'])

    return user
