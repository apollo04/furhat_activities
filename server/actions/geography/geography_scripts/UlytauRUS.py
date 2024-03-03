
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/KazakhstanMapRUS/UlytauRUS/Ulytau1.wav", "http://novators.kz/audio/KazakhstanMapRUS/UlytauRUS/Ulytau2.wav", "http://novators.kz/audio/KazakhstanMapRUS/UlytauRUS/Ulytau3.wav", "http://novators.kz/audio/KazakhstanMapRUS/UlytauRUS/Ulytau4.wav", "http://novators.kz/audio/KazakhstanMapRUS/UlytauRUS/Ulytau5.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
