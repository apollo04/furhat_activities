from typing import Any, List, Union

from fastapi import Depends
from pydantic import Field

from app.utils import AppModel
from .errors import InvalidCredentialsException

from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from .dependencies import parse_jwt_user_data
from app.parent.models import Parent
from app.specialist.models import Specialist


class GetMyAccountResponse(AppModel):
    id: Any = Field(alias="_id")
    email: str
    name: str
    surname: str
    role: str
    role_info: Union[Specialist, Parent, None]


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
    if user["role"] == "admin":
        user['role_info'] = None

    return user
