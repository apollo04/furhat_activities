from fastapi import Depends, HTTPException
from starlette.responses import Response

from app.utils import AppModel

from ..service import Service, get_service
from . import router

from ..models import CenterRequest


@router.patch("/center/{center_id:str}")
def update_center(
        center_id: str,
        input: CenterRequest,
        svc: Service = Depends(get_service),
) -> Response:
    update_result = svc.center_repository.update_center_by_id(
        center_id=center_id, data=input.dict()
    )
    if update_result.modified_count == 1:
        return Response(status_code=200)
    raise HTTPException(status_code=404, detail=f"Center {center_id} not found")
