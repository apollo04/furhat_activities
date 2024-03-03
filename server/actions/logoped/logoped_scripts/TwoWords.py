
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Isabel")
    
    url_list = ["http://novators.kz/audio/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ1.wav", "http://novators.kz/audio/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ2.wav", "http://novators.kz/audio/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ3.wav", "http://novators.kz/audio/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ4.wav", "http://novators.kz/audio/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ5.wav", "http://novators.kz/audio/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ6.wav", "http://novators.kz/audio/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ7.wav", "http://novators.kz/audio/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ8.wav", "http://novators.kz/audio/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ9.wav", "http://novators.kz/audio/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ10.wav", "http://novators.kz/audio/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ11.wav", "http://novators.kz/audio/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ12.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
