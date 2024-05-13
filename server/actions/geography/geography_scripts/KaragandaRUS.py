
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapRUS/KaragandaRUS/Karaganda1.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/KaragandaRUS/Karaganda2.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/KaragandaRUS/Karaganda3.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/KaragandaRUS/Karaganda4.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/KaragandaRUS/Karaganda5.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/KaragandaRUS/Karaganda6.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/KaragandaRUS/Karaganda7.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)