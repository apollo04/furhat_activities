from fastapi import APIRouter
import base64
import requests

router = APIRouter()

def read_actions(file_path):
    actions = []

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    current_name = None
    current_runner_file = None
    current_file = None
    current_icon_path = None

    for line in lines:
        if line.startswith('name:'):
            current_name = line.split(':')[1].strip().lower()
        elif line.startswith('runner_file:'):
            current_runner_file = line.split(':')[1].strip().lower()
        elif line.startswith('file:'):
            current_file = line.split(':')[1].strip().lower()
        elif line.startswith('icon:'):
            current_icon_path = line.split(':')[1].strip()
            try:
                with open("./mirai_actions/" + current_icon_path, "rb") as image_file:
                    current_icon_path = base64.encodebytes(image_file.read())
            except:
                current_icon_path = None
            actions.append({'category': current_name,
                                'runner_file': current_runner_file,
                                'file': current_file, 
                                'icon': current_icon_path, 
                                })

    return actions

actions = read_actions('mirai_actions/actions.txt')

@router.get("/")
def get_actions():
    return actions

from fastapi import HTTPException

@router.get("/actions/{runner_file}/{action_name}")
def send_request(action_name: str, ip: str, runner_file: str):
    action = next((a for a in actions if a['file'] == action_name), None)

    if action is None:
        raise HTTPException(status_code=404, detail="Action not found")

    url = f"http://{ip}/actions/{runner_file}/{action['file']}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.RequestException as e:
        return {'error': f'Request failed: {str(e)}'}

    return response.json()