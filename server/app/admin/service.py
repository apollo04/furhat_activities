from app.config import database

from .repository.center_repository import CenterRepository


class Service:
    def __init__(
            self,
            center_repository: CenterRepository,
    ):
        self.center_repository = center_repository


def get_service():
    center_repository = CenterRepository(database)

    svc = Service(center_repository)
    return svc
