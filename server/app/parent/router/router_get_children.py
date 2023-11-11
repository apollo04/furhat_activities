from typing import Any, List, Dict

from fastapi import Depends
from pydantic import Field

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service
from . import router


class ChildResponse(AppModel):
    id: Any = Field(alias="_id")
    center: str
    name: str
    surname: str
    age: int
    gender: str


class GetChildrenResponse(AppModel):
    children: List[ChildResponse]


@router.get("/children", response_model=GetChildrenResponse)
def get_children(
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, dict]:
    user_id = jwt_data.user_id
    children = svc.parentRepository.get_children(user_id)

    resp = {"children": children}

    return resp
