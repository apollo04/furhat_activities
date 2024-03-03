
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Isabel")
    
    url_list = ["http://novators.kz/audio/LogopedRUS/TwoWordsRUS/TwoWordsRUS1.wav", "http://novators.kz/audio/LogopedRUS/TwoWordsRUS/TwoWordsRUS2.wav", "http://novators.kz/audio/LogopedRUS/TwoWordsRUS/TwoWordsRUS3.wav", "http://novators.kz/audio/LogopedRUS/TwoWordsRUS/TwoWordsRUS4.wav", "http://novators.kz/audio/LogopedRUS/TwoWordsRUS/TwoWordsRUS5.wav", "http://novators.kz/audio/LogopedRUS/TwoWordsRUS/TwoWordsRUS6.wav", "http://novators.kz/audio/LogopedRUS/TwoWordsRUS/TwoWordsRUS7.wav", "http://novators.kz/audio/LogopedRUS/TwoWordsRUS/TwoWordsRUS8.wav", "http://novators.kz/audio/LogopedRUS/TwoWordsRUS/TwoWordsRUS9.wav", "http://novators.kz/audio/LogopedRUS/TwoWordsRUS/TwoWordsRUS10.wav", "http://novators.kz/audio/LogopedRUS/TwoWordsRUS/TwoWordsRUS11.wav", "http://novators.kz/audio/LogopedRUS/TwoWordsRUS/TwoWordsRUS12.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
