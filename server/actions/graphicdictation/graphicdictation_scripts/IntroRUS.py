
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/DictantRUS/IntroRUS/IntroRUS1.wav", "http://novators.kz/audio/DictantRUS/IntroRUS/IntroRUS2.wav", "http://novators.kz/audio/DictantRUS/IntroRUS/IntroRUS3.wav", "http://novators.kz/audio/DictantRUS/IntroRUS/IntroRUS4.wav", "http://novators.kz/audio/DictantRUS/IntroRUS/IntroRUS5.wav", "http://novators.kz/audio/DictantRUS/IntroRUS/IntroRUS6.wav", "http://novators.kz/audio/DictantRUS/IntroRUS/IntroRUS7.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
