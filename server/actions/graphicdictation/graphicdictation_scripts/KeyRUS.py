
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/DictantRUS/KeyRUS/Key1.wav", "http://novators.kz/audio/DictantRUS/KeyRUS/Key2.wav", "http://novators.kz/audio/DictantRUS/KeyRUS/Key3.wav", "http://novators.kz/audio/DictantRUS/KeyRUS/Key4.wav", "http://novators.kz/audio/DictantRUS/KeyRUS/Key5.wav", "http://novators.kz/audio/DictantRUS/KeyRUS/Key6.wav", "http://novators.kz/audio/DictantRUS/KeyRUS/Key7.wav", "http://novators.kz/audio/DictantRUS/KeyRUS/Key8.wav", "http://novators.kz/audio/DictantRUS/KeyRUS/Key9.wav", "http://novators.kz/audio/DictantRUS/KeyRUS/Key10.wav", "http://novators.kz/audio/DictantRUS/KeyRUS/Key11.wav", "http://novators.kz/audio/DictantRUS/KeyRUS/Key12.wav", "http://novators.kz/audio/DictantRUS/KeyRUS/Key13.wav", "http://novators.kz/audio/DictantRUS/KeyRUS/Key14.wav", "http://novators.kz/audio/DictantRUS/KeyRUS/Key15.wav", "http://novators.kz/audio/DictantRUS/KeyRUS/Key16.wav", "http://novators.kz/audio/DictantRUS/KeyRUS/Key17.wav", "http://novators.kz/audio/DictantRUS/KeyRUS/Key18.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
