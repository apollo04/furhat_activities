
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/DictantRUS/ElephantRUS/ElephantRUS1.wav", "http://novators.kz/audio/DictantRUS/ElephantRUS/ElephantRUS2.wav", "http://novators.kz/audio/DictantRUS/ElephantRUS/ElephantRUS3.wav", "http://novators.kz/audio/DictantRUS/ElephantRUS/ElephantRUS4.wav", "http://novators.kz/audio/DictantRUS/ElephantRUS/ElephantRUS5.wav", "http://novators.kz/audio/DictantRUS/ElephantRUS/ElephantRUS6.wav", "http://novators.kz/audio/DictantRUS/ElephantRUS/ElephantRUS7.wav", "http://novators.kz/audio/DictantRUS/ElephantRUS/ElephantRUS8.wav", "http://novators.kz/audio/DictantRUS/ElephantRUS/ElephantRUS9.wav", "http://novators.kz/audio/DictantRUS/ElephantRUS/ElephantRUS10.wav", "http://novators.kz/audio/DictantRUS/ElephantRUS/ElephantRUS11.wav", "http://novators.kz/audio/DictantRUS/ElephantRUS/ElephantRUS12.wav", "http://novators.kz/audio/DictantRUS/ElephantRUS/ElephantRUS13.wav", "http://novators.kz/audio/DictantRUS/ElephantRUS/ElephantRUS14.wav", "http://novators.kz/audio/DictantRUS/ElephantRUS/ElephantRUS15.wav", "http://novators.kz/audio/DictantRUS/ElephantRUS/ElephantRUS16.wav", "http://novators.kz/audio/DictantRUS/ElephantRUS/ElephantRUS17.wav", "http://novators.kz/audio/DictantRUS/ElephantRUS/ElephantRUS18.wav", "http://novators.kz/audio/DictantRUS/ElephantRUS/ElephantRUS19.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
