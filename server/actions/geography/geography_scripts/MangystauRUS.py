
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/KazakhstanMapRUS/MangystauRUS/Mangystau1.wav", "http://novators.kz/audio/KazakhstanMapRUS/MangystauRUS/Mangystau2.wav", "http://novators.kz/audio/KazakhstanMapRUS/MangystauRUS/Mangystau3.wav", "http://novators.kz/audio/KazakhstanMapRUS/MangystauRUS/Mangystau4.wav", "http://novators.kz/audio/KazakhstanMapRUS/MangystauRUS/Mangystau5.wav", "http://novators.kz/audio/KazakhstanMapRUS/MangystauRUS/Mangystau6.wav", "http://novators.kz/audio/KazakhstanMapRUS/MangystauRUS/Mangystau7.wav", "http://novators.kz/audio/KazakhstanMapRUS/MangystauRUS/Mangystau8.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
