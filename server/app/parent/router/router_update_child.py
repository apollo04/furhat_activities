from fastapi import Depends, HTTPException
from starlette.responses import Response

from ..service import Service, get_service
from . import router

from ..models import ChildRequest


@router.patch("/children/{child_id:str}")
def update_child(
        child_id: str,
        input: ChildRequest,
        svc: Service = Depends(get_service),
) -> Response:
    update_result = svc.child_repository.update_child_by_id(
        child_id=child_id, data=input.dict()
    )
    if update_result.modified_count == 1:
        return Response(status_code=200)
    raise HTTPException(status_code=404, detail=f"Child {child_id} not found")
