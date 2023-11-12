from datetime import datetime
from typing import List

from bson.objectid import ObjectId
from pymongo.database import Database
from pymongo.results import DeleteResult, UpdateResult

from ..models import Center


class CenterRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_center(self, input: dict) -> str:
        payload = {
            "name": input["name"],
            "country": input["name"],
            "city": input["name"],
            "street": input["name"],
            "created_at": datetime.utcnow(),
        }

        result = self.database["centers"].insert_one(payload)
        return result.inserted_id

    def get_centers(self) -> List[Center]:
        centers = self.database["centers"].find()
        return list(centers)

    def update_center_by_id(self, center_id: str, data: dict) -> UpdateResult:
        filter_query = {"_id": ObjectId(center_id)}
        update_query = {
            "$set": data,
        }

        return self.database["centers"].update_one(
            filter_query, update_query
        )

    def delete_center_by_id(self, center_id: str) -> DeleteResult:
        return self.database["centers"].delete_one(
            {"_id": ObjectId(center_id)}
        )
