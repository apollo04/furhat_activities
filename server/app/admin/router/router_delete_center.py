from fastapi import Depends, HTTPException
from starlette.responses import Response

from ..service import Service, get_service
from . import router


@router.delete("/center/{center_id:str}")
def delete_center(
        center_id: str,
        svc: Service = Depends(get_service),
) -> Response:
    delete_result = svc.center_repository.delete_center_by_id(center_id=center_id)

    if delete_result.deleted_count == 1:
        return Response(status_code=200)
    raise HTTPException(status_code=404, detail=f"Center {center_id} not found")
