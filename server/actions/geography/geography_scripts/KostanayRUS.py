
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/KazakhstanMapRUS/KostanayRUS/Kostanay1.wav", "http://novators.kz/audio/KazakhstanMapRUS/KostanayRUS/Kostanay2.wav", "http://novators.kz/audio/KazakhstanMapRUS/KostanayRUS/Kostanay3.wav", "http://novators.kz/audio/KazakhstanMapRUS/KostanayRUS/Kostanay4.wav", "http://novators.kz/audio/KazakhstanMapRUS/KostanayRUS/Kostanay5.wav", "http://novators.kz/audio/KazakhstanMapRUS/KostanayRUS/Kostanay6.wav", "http://novators.kz/audio/KazakhstanMapRUS/KostanayRUS/Kostanay7.wav", "http://novators.kz/audio/KazakhstanMapRUS/KostanayRUS/Kostanay8.wav", "http://novators.kz/audio/KazakhstanMapRUS/KostanayRUS/Kostanay9.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
