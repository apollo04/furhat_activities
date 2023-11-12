from fastapi import Depends

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data

from ..service import Service, get_service
from . import router

from ..models import Parent


@router.get("/", response_model=Parent)
def get_parent_by_user_id(
        jwt_data: JWTData = Depends(parse_jwt_user_data),
        svc: Service = Depends(get_service),
) -> Parent:
    user_id = jwt_data.user_id
    parent = svc.parent_repository.get_parent_by_user_id(user_id)
    return parent
