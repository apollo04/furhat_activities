from fastapi import Depends, HTTPException
from starlette.responses import Response

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data

from ..service import Service, get_service
from . import router


@router.delete("/children/{child_id:str}")
def delete_child(
        child_id: str,
        jwt_data: JWTData = Depends(parse_jwt_user_data),
        svc: Service = Depends(get_service),
) -> Response:
    user_id = jwt_data.user_id
    delete_result = svc.childRepository.delete_child_by_id(child_id=child_id)
    parent_delete_result = svc.parentRepository.delete_parents_child(user_id=user_id, child_id=child_id)

    if delete_result.deleted_count == 1 and parent_delete_result.modified_count == 1:
        return Response(status_code=200)
    raise HTTPException(status_code=404, detail=f"Child {child_id} not found")
