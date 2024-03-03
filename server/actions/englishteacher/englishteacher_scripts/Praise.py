
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jane")
    
    url_list = ["http://novators.kz/audio/EngTeacherKAZ/Praise/Praise1.wav", "http://novators.kz/audio/EngTeacherKAZ/Praise/Praise2.wav", "http://novators.kz/audio/EngTeacherKAZ/Praise/Praise3.wav", "http://novators.kz/audio/EngTeacherKAZ/Praise/Praise4.wav", "http://novators.kz/audio/EngTeacherKAZ/Praise/Praise5.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
