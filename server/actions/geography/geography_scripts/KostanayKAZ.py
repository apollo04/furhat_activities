
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/KazakhstanMapKAZ/KostanayKAZ/Kostanay1.wav", "http://novators.kz/audio/KazakhstanMapKAZ/KostanayKAZ/Kostanay2.wav", "http://novators.kz/audio/KazakhstanMapKAZ/KostanayKAZ/Kostanay3.wav", "http://novators.kz/audio/KazakhstanMapKAZ/KostanayKAZ/Kostanay4.wav", "http://novators.kz/audio/KazakhstanMapKAZ/KostanayKAZ/Kostanay5.wav", "http://novators.kz/audio/KazakhstanMapKAZ/KostanayKAZ/Kostanay6.wav", "http://novators.kz/audio/KazakhstanMapKAZ/KostanayKAZ/Kostanay7.wav", "http://novators.kz/audio/KazakhstanMapKAZ/KostanayKAZ/Kostanay8.wav", "http://novators.kz/audio/KazakhstanMapKAZ/KostanayKAZ/Kostanay9.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
