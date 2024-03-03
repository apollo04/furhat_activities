
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jane")
    
    url_list = ["http://novators.kz/audio/EngTeacherKAZ/OutroKAZ/OutroKAZ1.wav", "http://novators.kz/audio/EngTeacherKAZ/OutroKAZ/OutroENG1.wav", "http://novators.kz/audio/EngTeacherKAZ/OutroKAZ/OutroKAZ2.wav", "http://novators.kz/audio/EngTeacherKAZ/OutroKAZ/OutroENG2.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
