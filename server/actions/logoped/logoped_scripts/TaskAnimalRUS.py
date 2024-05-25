
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Isabel")
  
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/TaskRUS/TaskRUS2.wav", lipsync=True)