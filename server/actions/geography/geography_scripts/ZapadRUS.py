
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapRUS/ZapadRUS/Zapad1.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/ZapadRUS/Zapad2.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/ZapadRUS/Zapad3.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/ZapadRUS/Zapad4.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/ZapadRUS/Zapad5.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/ZapadRUS/Zapad6.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/ZapadRUS/Zapad7.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/ZapadRUS/Zapad8.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)