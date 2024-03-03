
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/DictantRUS/PraiseCorrectRUS/PraiseRUS1.wav", "http://novators.kz/audio/DictantRUS/PraiseCorrectRUS/PraiseRUS2.wav", "http://novators.kz/audio/DictantRUS/PraiseCorrectRUS/PraiseRUS3.wav", "http://novators.kz/audio/DictantRUS/PraiseCorrectRUS/PraiseRUS4.wav", "http://novators.kz/audio/DictantRUS/PraiseCorrectRUS/PraiseRUS5.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
