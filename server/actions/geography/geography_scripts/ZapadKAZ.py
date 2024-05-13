
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapKAZ/ZapadKAZ/Zapad1.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/ZapadKAZ/Zapad2.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/ZapadKAZ/Zapad3.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/ZapadKAZ/Zapad4.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/ZapadKAZ/Zapad5.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/ZapadKAZ/Zapad6.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/ZapadKAZ/Zapad7.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/ZapadKAZ/Zapad8.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
