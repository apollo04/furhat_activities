
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapKAZ/VostokKAZ/Vostok1.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/VostokKAZ/Vostok2.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/VostokKAZ/Vostok3.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/VostokKAZ/Vostok4.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/VostokKAZ/Vostok5.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/VostokKAZ/Vostok6.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/VostokKAZ/Vostok7.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/VostokKAZ/Vostok8.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/VostokKAZ/Vostok9.wav",
                "file:///home/furnix/resources/KazakhstanMapKAZ/VostokKAZ/Vostok10.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
