from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import uuid
import json

router = APIRouter()

database = {}

try:
    with open("data.json", "r") as json_file:
        database = json.load(json_file)
except FileNotFoundError:
    database = {"children": []}
    with open("data.json", "w") as json_file:
        json.dump(database, json_file)

def save_to_json():
    import json
    with open("data.json", "w") as json_file:
        json.dump(database, json_file)


class ChildCreate(BaseModel):
    name: str
    surname: str
    age: int
    gender: str

def get_child_by_id(child_id: str):
    try:
        return next(child for child in database["children"] if child["id"] == child_id)
    except StopIteration:
        return None

@router.post("/")
def create_child(child_data: ChildCreate):
    child = {"id": str(uuid.uuid4()), 
             "name": child_data.name, 
             "surname": child_data.surname, 
             "age": child_data.age, 
             "gender": child_data.gender, 
             "actions": []
            }
    database["children"].append(child)
    save_to_json()
    return child


@router.get("/")
def read_all_children():
    return {"children": database["children"]}

@router.get("/{child_id}")
def read_child(child_id: str):
    child = get_child_by_id(child_id)
    if child:
        return child
    else:
        raise HTTPException(status_code=404, detail="Child not found")

@router.delete("/{child_id}")
def delete_child(child_id: str):
    child = get_child_by_id(child_id)
    if child:
        database["children"].remove(child)
        save_to_json()
        return child
    else:
        raise HTTPException(status_code=404, detail="Child not found")