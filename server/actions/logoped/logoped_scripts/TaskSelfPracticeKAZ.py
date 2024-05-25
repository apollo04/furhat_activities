
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Isabel")
    
    furhat.say(url="file:///home/furnix/resources/LogopedKAZ/TaskKAZ/TaskKAZ5.wav", lipsync=True)