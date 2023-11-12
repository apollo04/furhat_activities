from app.config import database

from .repository.repository import ParentRepository
from .repository.child_repository import ChildRepository


class Service:
    def __init__(
            self,
            parent_repository: ParentRepository,
            child_repository: ChildRepository,
    ):
        self.parent_repository = parent_repository
        self.child_repository = child_repository


def get_service():
    parent_repository = ParentRepository(database)
    child_repository = ChildRepository(database)

    svc = Service(parent_repository=parent_repository, child_repository=child_repository)
    return svc
