from typing import Any, List

from fastapi import Depends
from pydantic import Field

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service
from . import router

from ..models import Specialist


@router.get("/", response_model=Specialist)
def get_specialist_by_user_id(
        jwt_data: JWTData = Depends(parse_jwt_user_data),
        svc: Service = Depends(get_service),
) -> Specialist:
    user_id = jwt_data.user_id
    specialist = svc.repository.get_specialist_by_user_id(user_id)
    return specialist
