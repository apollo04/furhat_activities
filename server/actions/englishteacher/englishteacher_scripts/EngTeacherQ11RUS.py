
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jane")
    
    url_list = ["http://novators.kz/audio/EngTeacherRUS/Q11RUS/Q11RUS.wav", "http://novators.kz/audio/EngTeacherRUS/Q11RUS/Q11ENG.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
