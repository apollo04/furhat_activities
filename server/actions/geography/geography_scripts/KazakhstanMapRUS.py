
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/KazakhstanMapRUS/APP1.wav", "http://novators.kz/audio/KazakhstanMapRUS/APP2.wav", "http://novators.kz/audio/KazakhstanMapRUS/APP3.wav", "http://novators.kz/audio/KazakhstanMapRUS/APP4.wav", "http://novators.kz/audio/KazakhstanMapRUS/APP5.wav", "http://novators.kz/audio/KazakhstanMapRUS/APP6.wav", "http://novators.kz/audio/KazakhstanMapRUS/APP7.wav", "http://novators.kz/audio/KazakhstanMapRUS/APP8.wav", "http://novators.kz/audio/KazakhstanMapRUS/APP9.wav", "http://novators.kz/audio/KazakhstanMapRUS/APP10.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
