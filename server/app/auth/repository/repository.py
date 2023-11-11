from datetime import datetime
from typing import Optional

from bson.objectid import ObjectId
from pymongo.database import Database

from ..utils.security import hash_password


class AuthRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_user(self, user: dict):
        payload = {
            "email": user["email"],
            "role": user["role"],
            "name": user["name"],
            "surname": user["surname"],
            "password": hash_password(user["password"]),
            "created_at": datetime.utcnow(),
        }

        result = self.database["users"].insert_one(payload)

        if result.acknowledged:
            inserted_id = result.inserted_id
            user = self.database["users"].find_one({'_id': inserted_id})
            return user

    def get_user_by_id(self, user_id: str) -> Optional[dict]:
        user = self.database["users"].find_one(
            {
                "_id": ObjectId(user_id),
            }
        )
        return user

    def get_user_by_email(self, email: str) -> Optional[dict]:
        user = self.database["users"].find_one(
            {
                "email": email,
            }
        )
        return user
