from fastapi import Depends

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data

from ..service import Service, get_service
from . import router

from ..models import ChildRequest


@router.post("/children", response_model=str)
def add_child(
        input: ChildRequest,
        jwt_data: JWTData = Depends(parse_jwt_user_data),
        svc: Service = Depends(get_service),
) -> str:
    user_id = jwt_data.user_id

    parent = svc.parent_repository.get_parent_by_user_id(user_id=user_id)

    input = input.dict()
    input['center'] = parent['center']
    input['parent_id'] = parent['_id']

    child_id = svc.child_repository.create_child(input)
    svc.parent_repository.add_child_to_parent(user_id=user_id, child_id=child_id)

    return str(child_id)
