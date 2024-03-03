
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/KazakhstanMapRUS/TurkestanRUS/Turkestan1.wav", "http://novators.kz/audio/KazakhstanMapRUS/TurkestanRUS/Turkestan2.wav", "http://novators.kz/audio/KazakhstanMapRUS/TurkestanRUS/Turkestan3.wav", "http://novators.kz/audio/KazakhstanMapRUS/TurkestanRUS/Turkestan4.wav", "http://novators.kz/audio/KazakhstanMapRUS/TurkestanRUS/Turkestan5.wav", "http://novators.kz/audio/KazakhstanMapRUS/TurkestanRUS/Turkestan6.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
