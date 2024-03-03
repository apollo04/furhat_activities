
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/KazakhstanMapKAZ/MangystauKAZ/Mangystau1.wav", "http://novators.kz/audio/KazakhstanMapKAZ/MangystauKAZ/Mangystau2.wav", "http://novators.kz/audio/KazakhstanMapKAZ/MangystauKAZ/Mangystau3.wav", "http://novators.kz/audio/KazakhstanMapKAZ/MangystauKAZ/Mangystau4.wav", "http://novators.kz/audio/KazakhstanMapKAZ/MangystauKAZ/Mangystau5.wav", "http://novators.kz/audio/KazakhstanMapKAZ/MangystauKAZ/Mangystau6.wav", "http://novators.kz/audio/KazakhstanMapKAZ/MangystauKAZ/Mangystau7.wav", "http://novators.kz/audio/KazakhstanMapKAZ/MangystauKAZ/Mangystau8.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
