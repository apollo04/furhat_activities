
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/KazakhstanMapKAZ/UlytauKAZ/Ulytau1.wav", "http://novators.kz/audio/KazakhstanMapKAZ/UlytauKAZ/Ulytau2.wav", "http://novators.kz/audio/KazakhstanMapKAZ/UlytauKAZ/Ulytau3.wav", "http://novators.kz/audio/KazakhstanMapKAZ/UlytauKAZ/Ulytau4.wav", "http://novators.kz/audio/KazakhstanMapKAZ/UlytauKAZ/Ulytau5.wav", "http://novators.kz/audio/KazakhstanMapKAZ/UlytauKAZ/Ulytau6.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
