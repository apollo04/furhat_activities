
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/KazakhstanMapKAZ/TurkestanKAZ/Turkestan1.wav", "http://novators.kz/audio/KazakhstanMapKAZ/TurkestanKAZ/Turkestan2.wav", "http://novators.kz/audio/KazakhstanMapKAZ/TurkestanKAZ/Turkestan3.wav", "http://novators.kz/audio/KazakhstanMapKAZ/TurkestanKAZ/Turkestan4.wav", "http://novators.kz/audio/KazakhstanMapKAZ/TurkestanKAZ/Turkestan5.wav", "http://novators.kz/audio/KazakhstanMapKAZ/TurkestanKAZ/Turkestan6.wav", "http://novators.kz/audio/KazakhstanMapKAZ/TurkestanKAZ/Turkestan7.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
