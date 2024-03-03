
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/KazakhstanMapKAZ/APP1.wav", "http://novators.kz/audio/KazakhstanMapKAZ/APP2.wav", "http://novators.kz/audio/KazakhstanMapKAZ/APP3.wav", "http://novators.kz/audio/KazakhstanMapKAZ/APP4.wav", "http://novators.kz/audio/KazakhstanMapKAZ/APP5.wav", "http://novators.kz/audio/KazakhstanMapKAZ/APP6.wav", "http://novators.kz/audio/KazakhstanMapKAZ/APP7.wav", "http://novators.kz/audio/KazakhstanMapKAZ/APP8.wav", "http://novators.kz/audio/KazakhstanMapKAZ/APP9.wav", "http://novators.kz/audio/KazakhstanMapKAZ/APP10.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
