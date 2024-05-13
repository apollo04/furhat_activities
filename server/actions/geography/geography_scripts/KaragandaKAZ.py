
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapKAZ/KaragandaKAZ/Karaganda1.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/KaragandaKAZ/Karaganda2.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/KaragandaKAZ/Karaganda3.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/KaragandaKAZ/Karaganda4.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/KaragandaKAZ/Karaganda5.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/KaragandaKAZ/Karaganda6.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/KaragandaKAZ/Karaganda7.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)