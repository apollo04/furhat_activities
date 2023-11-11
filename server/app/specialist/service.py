from app.config import database

from .repository.repository import SpecialistRepository


class Service:
    def __init__(
            self,
            repository: SpecialistRepository,
    ):
        self.repository = repository


def get_service():
    repository = SpecialistRepository(database)

    svc = Service(repository)
    return svc
