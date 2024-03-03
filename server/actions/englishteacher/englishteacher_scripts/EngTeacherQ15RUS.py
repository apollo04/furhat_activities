
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jane")
    
    url_list = ["http://novators.kz/audio/EngTeacherRUS/Q15RUS/Q15RUS.wav", "http://novators.kz/audio/EngTeacherRUS/Q15RUS/Q15ENG.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
