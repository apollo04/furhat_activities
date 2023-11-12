from typing import Any, List

from pydantic import Field

from app.utils import AppModel


class Specialist(AppModel):
    id: Any = Field(alias="_id")
    school: str
    children: List[str]
