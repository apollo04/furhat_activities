from fastapi import Depends

from ..service import Service, get_service
from . import router

from ..models import CenterRequest


@router.post("/center", response_model=str)
def add_center(
        input: CenterRequest,
        svc: Service = Depends(get_service),
) -> str:
    input = input.dict()
    center_id = svc.center_repository.create_center(input)

    return center_id
