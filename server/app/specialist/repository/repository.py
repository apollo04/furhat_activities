from datetime import datetime

from bson.objectid import ObjectId
from pymongo.database import Database
from ..models import Specialist

class SpecialistRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_specialist(self, input: dict):
        payload = {
            "children": [],
            "center": input["center"],
            "user_id": ObjectId(input["user_id"]),
            "created_at": datetime.utcnow(),
        }

        self.database["specialists"].insert_one(payload)

    def get_specialist_by_user_id(self, user_id: str) -> Specialist:
        specialist = self.database["specialists"].find_one(
            {
                "user_id": ObjectId(user_id),
            }
        )
        return specialist
