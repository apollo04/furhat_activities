from typing import Any

from pydantic import Field

from app.utils import AppModel


class CenterRequest(AppModel):
    name: str
    country: str
    city: str
    street: str


class Center(AppModel):
    id: Any = Field(alias="_id")
    name: str
    country: str
    city: str
    street: str

