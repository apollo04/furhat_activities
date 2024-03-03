
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/KazakhstanMapKAZ/AlmatyKAZ/Almaty1.wav", "http://novators.kz/audio/KazakhstanMapKAZ/AlmatyKAZ/Almaty2.wav", "http://novators.kz/audio/KazakhstanMapKAZ/AlmatyKAZ/Almaty3.wav", "http://novators.kz/audio/KazakhstanMapKAZ/AlmatyKAZ/Almaty4.wav", "http://novators.kz/audio/KazakhstanMapKAZ/AlmatyKAZ/Almaty5.wav", "http://novators.kz/audio/KazakhstanMapKAZ/AlmatyKAZ/Almaty6.wav", "http://novators.kz/audio/KazakhstanMapKAZ/AlmatyKAZ/Almaty7.wav", "http://novators.kz/audio/KazakhstanMapKAZ/AlmatyKAZ/Almaty8.wav", "http://novators.kz/audio/KazakhstanMapKAZ/AlmatyKAZ/Almaty9.wav", "http://novators.kz/audio/KazakhstanMapKAZ/AlmatyKAZ/Almaty10.wav", "http://novators.kz/audio/KazakhstanMapKAZ/AlmatyKAZ/Almaty11.wav", "http://novators.kz/audio/KazakhstanMapKAZ/AlmatyKAZ/Almaty12.wav", "http://novators.kz/audio/KazakhstanMapKAZ/AlmatyKAZ/Almaty13.wav", "http://novators.kz/audio/KazakhstanMapKAZ/AlmatyKAZ/Almaty14.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
