from fastapi import APIRouter
from furhat_remote_api import FurhatRemoteAPI

router = APIRouter()

@router.get("/{ip}/stop/")
def stop_furhat(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.say_stop()
