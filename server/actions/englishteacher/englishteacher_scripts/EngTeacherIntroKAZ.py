
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jane")
    
    url_list = ["http://novators.kz/audio/EngTeacherKAZ/IntroKAZ/IntroKAZ1.wav", "http://novators.kz/audio/EngTeacherKAZ/IntroKAZ/IntroENG1.wav", "http://novators.kz/audio/EngTeacherKAZ/IntroKAZ/IntroKAZ2.wav", "http://novators.kz/audio/EngTeacherKAZ/IntroKAZ/IntroENG2.wav", "http://novators.kz/audio/EngTeacherKAZ/IntroKAZ/IntroKAZ3.wav", "http://novators.kz/audio/EngTeacherKAZ/IntroKAZ/IntroENG3.wav", "http://novators.kz/audio/EngTeacherKAZ/IntroKAZ/IntroKAZ4.wav", "http://novators.kz/audio/EngTeacherKAZ/IntroKAZ/IntroENG4.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
