from typing import Any, List, Dict

from fastapi import Depends
from pydantic import Field

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service
from . import router


class ParentResponce(AppModel):
    id: Any = Field(alias="_id")
    center: str
    children: List[str]


class GetParentByIdResponse(AppModel):
    parent: ParentResponce


@router.get("/", response_model=GetParentByIdResponse)
def get_parent_by_user_id(
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, dict]:
    user_id = jwt_data.user_id
    parent = svc.parentRepository.get_parent_by_user_id(user_id)

    resp = {"parent": parent}

    return resp
