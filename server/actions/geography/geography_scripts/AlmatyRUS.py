
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/KazakhstanMapRUS/AlmatyRUS/Almaty1.wav", "http://novators.kz/audio/KazakhstanMapRUS/AlmatyRUS/Almaty2.wav", "http://novators.kz/audio/KazakhstanMapRUS/AlmatyRUS/Almaty3.wav", "http://novators.kz/audio/KazakhstanMapRUS/AlmatyRUS/Almaty4.wav", "http://novators.kz/audio/KazakhstanMapRUS/AlmatyRUS/Almaty5.wav", "http://novators.kz/audio/KazakhstanMapRUS/AlmatyRUS/Almaty6.wav", "http://novators.kz/audio/KazakhstanMapRUS/AlmatyRUS/Almaty7.wav", "http://novators.kz/audio/KazakhstanMapRUS/AlmatyRUS/Almaty8.wav", "http://novators.kz/audio/KazakhstanMapRUS/AlmatyRUS/Almaty9.wav", "http://novators.kz/audio/KazakhstanMapRUS/AlmatyRUS/Almaty10.wav", "http://novators.kz/audio/KazakhstanMapRUS/AlmatyRUS/Almaty11.wav", "http://novators.kz/audio/KazakhstanMapRUS/AlmatyRUS/Almaty12.wav", "http://novators.kz/audio/KazakhstanMapRUS/AlmatyRUS/Almaty13.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
