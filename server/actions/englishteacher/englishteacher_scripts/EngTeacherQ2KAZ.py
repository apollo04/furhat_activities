
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jane")
    
    url_list = ["http://novators.kz/audio/EngTeacherKAZ/Q2KAZ/Q2KAZ.wav", "http://novators.kz/audio/EngTeacherKAZ/Q2KAZ/Q2ENG.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
