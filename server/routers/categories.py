from fastapi import APIRouter
import uuid
import importlib.util
import base64

router = APIRouter()

actions = {}

def read_actions_file(current_folder, file_path):
    actions_list = []
    current_action = None
    current_file = None

    with open("./actions/" + file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        if line.startswith('action:'):
            current_action = line.split(':')[1].strip()
        elif line.startswith('icon:'):
            current_icon_path = line.split(':')[1].strip()
            try:
                with open("./actions/" + current_folder + current_icon_path, "rb") as image_file:
                    current_icon_path = base64.encodebytes(image_file.read())
            except:
                current_icon_path = ""
        elif line.startswith('file:'):
            current_file = line.split(':')[1].strip()
            actions_list.append({"id": str(uuid.uuid4()), 'action': current_action, 'file': current_file, 'icon': current_icon_path})

    return actions_list

def read_grade_names(file_path):
    grade_names = []

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        grade_names.append(line.strip())

    return grade_names

def read_categories(file_path):
    categories = []

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    current_category = None
    current_file_kaz = None
    current_file_rus = None
    current_icon_path = None
    current_folder = None
    current_grade_names = None

    for line in lines:
        if line.startswith('category:'):
            current_category = line.split(':')[1].strip().lower()
            actions[current_category] = {}
        elif line.startswith('icon:'):
            current_icon_path = line.split(':')[1].strip()
            with open("./actions/" + current_icon_path, "rb") as image_file:
                current_icon_path = base64.encodebytes(image_file.read())
        elif line.startswith('folder:'):
            current_folder = line.split(':')[1].strip()
        elif line.startswith('file_kaz:'):
            current_file_kaz = line.split(':')[1].strip()
            actions[current_category]["actions_kaz"] = read_actions_file(current_folder, current_file_kaz)
        elif line.startswith('file_rus:'):
            current_file_rus = line.split(':')[1].strip()
            actions[current_category]["actions_rus"] = read_actions_file(current_folder, current_file_rus)
        elif line.startswith('grade_names:'):
            current_grade_names = line.split(':')[1].strip()
            current_grade_names = read_grade_names("./actions/" + current_grade_names)
            actions[current_category]["grade_names"] = current_grade_names
            categories.append({'category': current_category, 
                               'file_kaz': current_file_kaz, 
                               'file_rus': current_file_rus, 
                               'icon': current_icon_path, 
                               'folder': current_folder, 
                               'grade_names': current_grade_names
                               })

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
def run_action(category_name: str, action_id: str, ip: str):
    all_actions = actions[category_name]["actions_kaz"] + actions[category_name]["actions_rus"]

    category = [x for x in categories if x["category"] == category_name][0]

    for action in all_actions:
        if action["id"] == action_id:
            file_name = action["file"]

            print("running action " + file_name)

            spec = importlib.util.spec_from_file_location(file_name, "actions/" + category["folder"] + file_name)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "run_action") and callable(module.run_action):
                module.run_action(ip)
                return {"success": f"Action {action_id} executed for IP {ip}"}

    return {"error": "Action not found or run_action function not present in the module"}