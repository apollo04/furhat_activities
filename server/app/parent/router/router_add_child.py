from typing import Any

from fastapi import Depends
from pydantic import Field

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data

from ..service import Service, get_service
from . import router

from ...utils import AppModel


class AddChildRequest(AppModel):
    name: str
    surname: str
    age: int
    gender: str


class AddChildResponse(AppModel):
    id: Any = Field(alias="_id")


@router.post("/children", response_model=AddChildResponse)
def add_child(
        input: AddChildRequest,
        jwt_data: JWTData = Depends(parse_jwt_user_data),
        svc: Service = Depends(get_service),
) -> AddChildResponse:
    user_id = jwt_data.user_id

    parent = svc.parentRepository.get_parent_by_user_id(user_id=user_id)

    input = input.dict()
    input['center'] = parent['center']
    input['parent_id'] = parent['_id']

    child_id = svc.childRepository.create_child(input)
    svc.parentRepository.add_child_to_parent(user_id=user_id, child_id=child_id)

    return AddChildResponse(id=child_id)
