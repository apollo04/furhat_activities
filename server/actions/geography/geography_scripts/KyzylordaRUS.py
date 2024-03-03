
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/KazakhstanMapRUS/KyzylordaRUS/Kyzylorda1.wav", "http://novators.kz/audio/KazakhstanMapRUS/KyzylordaRUS/Kyzylorda2.wav", "http://novators.kz/audio/KazakhstanMapRUS/KyzylordaRUS/Kyzylorda3.wav", "http://novators.kz/audio/KazakhstanMapRUS/KyzylordaRUS/Kyzylorda4.wav", "http://novators.kz/audio/KazakhstanMapRUS/KyzylordaRUS/Kyzylorda5.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
