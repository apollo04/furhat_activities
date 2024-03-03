
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/DictantKAZ/IntroKAZ/IntroKAZ1.wav", "http://novators.kz/audio/DictantKAZ/IntroKAZ/IntroKAZ2.wav", "http://novators.kz/audio/DictantKAZ/IntroKAZ/IntroKAZ3.wav", "http://novators.kz/audio/DictantKAZ/IntroKAZ/IntroKAZ4.wav", "http://novators.kz/audio/DictantKAZ/IntroKAZ/IntroKAZ5.wav", "http://novators.kz/audio/DictantKAZ/IntroKAZ/IntroKAZ6.wav", "http://novators.kz/audio/DictantKAZ/IntroKAZ/IntroKAZ7.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
