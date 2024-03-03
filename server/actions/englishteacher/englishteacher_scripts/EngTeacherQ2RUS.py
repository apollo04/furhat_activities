
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jane")
    
    url_list = ["http://novators.kz/audio/EngTeacherRUS/Q2RUS/Q2RUS.wav", "http://novators.kz/audio/EngTeacherRUS/Q2RUS/Q2ENG.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
