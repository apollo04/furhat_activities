from typing import List

from fastapi import Depends

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data

from ..service import Service, get_service
from . import router

from ..models import Child


@router.get("/children/{center_id:str}", response_model=List[Child])
def get_children_by_center_id(
        center_id: str,
        svc: Service = Depends(get_service),
) -> List[Child]:
    children = svc.child_repository.get_child_by_center_id(center_id)
    return children
