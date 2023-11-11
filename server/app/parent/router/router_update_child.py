from fastapi import Depends, Response, HTTPException
from starlette.responses import Response

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service
from . import router


class UpdateChildrenRequest(AppModel):
    name: str
    surname: str
    age: int
    gender: str


@router.patch("/children/{child_id:str}")
def update_child(
    child_id: str,
    input: UpdateChildrenRequest,
    svc: Service = Depends(get_service),
) -> Response:
    update_result = svc.childRepository.update_child_by_id(
        child_id=child_id, data=input.dict()
    )
    if update_result.modified_count == 1:
        return Response(status_code=200)
    raise HTTPException(status_code=404, detail=f"Child {child_id} not found")
