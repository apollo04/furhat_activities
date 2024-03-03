
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Isabel")
    
    url_list = ["http://novators.kz/audio/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS1.wav", "http://novators.kz/audio/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS2.wav", "http://novators.kz/audio/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS3.wav", "http://novators.kz/audio/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS4.wav", "http://novators.kz/audio/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS5.wav", "http://novators.kz/audio/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS6.wav", "http://novators.kz/audio/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS7.wav", "http://novators.kz/audio/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS8.wav", "http://novators.kz/audio/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS9.wav", "http://novators.kz/audio/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS10.wav", "http://novators.kz/audio/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS11.wav", "http://novators.kz/audio/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS12.wav", "http://novators.kz/audio/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS13.wav", "http://novators.kz/audio/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS14.wav", "http://novators.kz/audio/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS15.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
