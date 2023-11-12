from typing import Any, List

from pydantic import Field

from app.utils import AppModel


class ChildRequest(AppModel):
    name: str
    surname: str
    age: int
    gender: str


class AddChildResponse(AppModel):
    id: Any = Field(alias="_id")


class Child(AppModel):
    id: Any = Field(alias="_id")
    center: str
    name: str
    surname: str
    age: int
    gender: str


class Parent(AppModel):
    id: Any = Field(alias="_id")
    center: str
    children: List[str]
