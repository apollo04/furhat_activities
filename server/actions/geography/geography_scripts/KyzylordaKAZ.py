
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/KazakhstanMapKAZ/KyzylordaKAZ/Kyzylorda1.wav", "http://novators.kz/audio/KazakhstanMapKAZ/KyzylordaKAZ/Kyzylorda2.wav", "http://novators.kz/audio/KazakhstanMapKAZ/KyzylordaKAZ/Kyzylorda3.wav", "http://novators.kz/audio/KazakhstanMapKAZ/KyzylordaKAZ/Kyzylorda4.wav", "http://novators.kz/audio/KazakhstanMapKAZ/KyzylordaKAZ/Kyzylorda5.wav", "http://novators.kz/audio/KazakhstanMapKAZ/KyzylordaKAZ/Kyzylorda6.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
