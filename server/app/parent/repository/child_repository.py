from datetime import datetime
from typing import List

from bson.objectid import ObjectId
from pymongo.database import Database
from pymongo.results import DeleteResult, UpdateResult


class ChildRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_child(self, input: dict) -> str:
        payload = {
            "name": input["name"],
            "surname": input["surname"],
            "age": input["age"],
            "gender": input["gender"],
            "center": input["center"],
            "parent_id": ObjectId(input["parent_id"]),
            "created_at": datetime.utcnow(),
        }

        result = self.database["children"].insert_one(payload)
        return result.inserted_id

    def get_child_by_parent_id(self, parent_id: str) -> dict:
        child = self.database["children"].find_one(
            {
                "parent_id": ObjectId(parent_id),
            }
        )
        return child

    def get_children_by_parent_id(self, parent_id: str) -> List[dict]:
        child = self.database["children"].find(
            {
                "parent_id": ObjectId(parent_id),
            }
        )
        return list(child)

    def update_child_by_id(self, child_id: str, data: dict) -> UpdateResult:
        filter_query = {"_id": ObjectId(child_id)}
        update_query = {
            "$set": data,
        }

        return self.database["children"].update_one(
            filter_query, update_query
        )

    def delete_child_by_id(self, child_id: str) -> DeleteResult:
        return self.database["children"].delete_one(
            {"_id": ObjectId(child_id)}
        )
