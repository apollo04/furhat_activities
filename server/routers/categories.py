from fastapi import APIRouter
import uuid
import importlib.util

router = APIRouter()

actions = {}

def read_actions_file(file_path):
    actions_list = []
    current_action = None
    current_file = None

    with open("actions/" + file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        if line.startswith('action:'):
            current_action = line.split(':')[1].strip()
        elif line.startswith('icon:'):
            current_icon = line.split(':')[1].strip()
        elif line.startswith('file:'):
            current_file = line.split(':')[1].strip()
            actions_list.append({"id": str(uuid.uuid4()), 'action': current_action, 'file': current_file, 'icon': current_icon})

    return actions_list

def read_categories(file_path):
    categories = []

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    current_category = None
    current_file_kaz = None
    current_file_rus = None
    current_icon = None

    for line in lines:
        if line.startswith('category:'):
            current_category = line.split(':')[1].strip().lower()
            actions[current_category] = {}
        elif line.startswith('icon:'):
            current_icon = line.split(':')[1].strip()
        elif line.startswith('file_kaz:'):
            current_file_kaz = line.split(':')[1].strip()
            actions[current_category]["actions_kaz"] = read_actions_file(current_file_kaz)
        elif line.startswith('file_rus:'):
            current_file_rus = line.split(':')[1].strip()
            actions[current_category]["actions_rus"] = read_actions_file(current_file_rus)
            categories.append({'category': current_category, 'file_kaz': current_file_kaz, 'file_rus': current_file_rus, 'icon': current_icon})

    return categories

categories = read_categories('actions/categories.txt')

@router.get("/")
def get_categories():
    return categories

@router.get("/{category_name}/actions")
def read_category_actions(category_name: str):
    actions_list_kaz = actions[category_name.lower()]["actions_kaz"]
    actions_list_rus = actions[category_name.lower()]["actions_rus"]

    return {"category_name": category_name, "actions_kaz": actions_list_kaz, "actions_rus": actions_list_rus}

@router.get("/{category_name}/actions/{action_id}")
def read_action(category_name: str, action_id: str, ip: str):
    for action in actions[category_name]["actions_kaz"]:
        if action["id"] == action_id:
            file_name = action["file"]
            spec = importlib.util.spec_from_file_location(file_name, f"{file_name}.py")
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "run_action") and callable(module.run_action):
                module.run_action(ip)
                return {"success": f"Action {action_id} executed for IP {ip}"}

    return {"error": "Action not found or run_action function not present in the module"}