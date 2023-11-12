from datetime import datetime
from typing import List

from bson.objectid import ObjectId
from pymongo.database import Database
from pymongo.results import UpdateResult

from ..models import Child, Parent


class ParentRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_parent(self, input: dict):
        payload = {
            "children": [],
            "center": input["center"],
            "user_id": ObjectId(input["user_id"]),
            "created_at": datetime.utcnow(),
        }

        self.database["parents"].insert_one(payload)

    def add_child_to_parent(self, user_id: str, child_id: str) -> UpdateResult:
        filter_query = {"user_id": ObjectId(user_id)}
        update_query = {"$push": {"children": ObjectId(child_id)}}

        return self.database["parents"].update_one(
            filter_query,
            update_query
        )

    def delete_parents_child(self, user_id: str, child_id: str) -> UpdateResult:
        filter_query = {"user_id": ObjectId(user_id)}
        update_query = {"$pull": {"children": ObjectId(child_id)}}

        return self.database["parents"].update_one(
            filter_query,
            update_query
        )

    def get_parent_by_user_id(self, user_id: str) -> Parent:
        parent = self.database["parents"].find_one(
            {
                "user_id": ObjectId(user_id),
            }
        )
        return parent

    def get_children(self, user_id: str) -> List[Child]:
        parent = self.database["parents"].find_one(
            {
                "user_id": ObjectId(user_id),
            }
        )
        children = []

        if parent:
            children = parent.get("children", [])
        return children
