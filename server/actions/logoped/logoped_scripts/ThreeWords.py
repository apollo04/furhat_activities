
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Isabel")
    
    url_list = ["http://novators.kz/audio/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ1.wav", "http://novators.kz/audio/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ2.wav", "http://novators.kz/audio/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ3.wav", "http://novators.kz/audio/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ4.wav", "http://novators.kz/audio/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ5.wav", "http://novators.kz/audio/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ6.wav", "http://novators.kz/audio/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ7.wav", "http://novators.kz/audio/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ8.wav", "http://novators.kz/audio/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ9.wav", "http://novators.kz/audio/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ10.wav", "http://novators.kz/audio/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ11.wav", "http://novators.kz/audio/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ12.wav", "http://novators.kz/audio/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ13.wav", "http://novators.kz/audio/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ14.wav", "http://novators.kz/audio/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ15.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
