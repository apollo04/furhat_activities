
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapKAZ/KostanayKAZ/Kostanay1.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/KostanayKAZ/Kostanay2.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/KostanayKAZ/Kostanay3.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/KostanayKAZ/Kostanay4.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/KostanayKAZ/Kostanay5.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/KostanayKAZ/Kostanay6.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/KostanayKAZ/Kostanay7.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/KostanayKAZ/Kostanay8.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/KostanayKAZ/Kostanay9.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
