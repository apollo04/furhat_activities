from pydantic import BaseSettings

from .adapters.jwt_service import JwtService
from .repository.repository import AuthRepository

from app.config import database
from ..specialist.repository.repository import SpecialistRepository
from ..parent.repository.repository import ParentRepository


class AuthConfig(BaseSettings):
    JWT_ALG: str = "HS256"
    JWT_SECRET: str = "YOUR_SUPER_SECRET_STRING"
    JWT_EXP: int = 10_800


config = AuthConfig()

class Service:
    def __init__(
        self,
        authRepository: AuthRepository,
        specialistRepository: SpecialistRepository,
        parentRepository: ParentRepository,
        jwt_svc: JwtService,
    ):
        self.specialistRepository = specialistRepository
        self.parentRepository = parentRepository
        self.authRepository = authRepository
        self.jwt_svc = jwt_svc


def get_service():
    authRepository = AuthRepository(database)
    jwt_svc = JwtService(config.JWT_ALG, config.JWT_SECRET, config.JWT_EXP)
    specialistRepository= SpecialistRepository(database)
    parentRepository= ParentRepository(database)

    svc = Service(specialistRepository=specialistRepository, parentRepository=parentRepository, authRepository=authRepository, jwt_svc=jwt_svc)
    return svc
