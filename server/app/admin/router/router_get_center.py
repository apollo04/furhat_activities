from typing import List

from fastapi import Depends

from ..service import Service, get_service
from . import router

from ..models import Center


@router.get("/center", response_model=List[Center])
def get_centers(
        svc: Service = Depends(get_service),
) -> List[Center]:
    centers = svc.center_repository.get_centers()
    return centers
