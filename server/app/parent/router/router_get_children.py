from typing import List

from fastapi import Depends

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data

from ..service import Service, get_service
from . import router

from ..models import Child


@router.get("/children", response_model=List[Child])
def get_children(
        jwt_data: JWTData = Depends(parse_jwt_user_data),
        svc: Service = Depends(get_service),
) -> List[Child]:
    user_id = jwt_data.user_id
    children = svc.parent_repository.get_children(user_id)
    return children
