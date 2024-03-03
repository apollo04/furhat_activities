
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/DictantKAZ/KeyKAZ/Key1.wav", "http://novators.kz/audio/DictantKAZ/KeyKAZ/Key2.wav", "http://novators.kz/audio/DictantKAZ/KeyKAZ/Key3.wav", "http://novators.kz/audio/DictantKAZ/KeyKAZ/Key4.wav", "http://novators.kz/audio/DictantKAZ/KeyKAZ/Key5.wav", "http://novators.kz/audio/DictantKAZ/KeyKAZ/Key6.wav", "http://novators.kz/audio/DictantKAZ/KeyKAZ/Key7.wav", "http://novators.kz/audio/DictantKAZ/KeyKAZ/Key8.wav", "http://novators.kz/audio/DictantKAZ/KeyKAZ/Key9.wav", "http://novators.kz/audio/DictantKAZ/KeyKAZ/Key10.wav", "http://novators.kz/audio/DictantKAZ/KeyKAZ/Key11.wav", "http://novators.kz/audio/DictantKAZ/KeyKAZ/Key12.wav", "http://novators.kz/audio/DictantKAZ/KeyKAZ/Key13.wav", "http://novators.kz/audio/DictantKAZ/KeyKAZ/Key14.wav", "http://novators.kz/audio/DictantKAZ/KeyKAZ/Key15.wav", "http://novators.kz/audio/DictantKAZ/KeyKAZ/Key16.wav", "http://novators.kz/audio/DictantKAZ/KeyKAZ/Key17.wav", "http://novators.kz/audio/DictantKAZ/KeyKAZ/Key18.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
