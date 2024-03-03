
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jane")
    
    url_list = ["http://novators.kz/audio/EngTeacherKAZ/Q1KAZ/Q1KAZ.wav", "http://novators.kz/audio/EngTeacherKAZ/Q1KAZ/Q1ENG.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
