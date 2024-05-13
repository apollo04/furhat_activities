
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapKAZ/AtyrauKAZ/Atyrau1.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AtyrauKAZ/Atyrau2.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AtyrauKAZ/Atyrau3.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AtyrauKAZ/Atyrau4.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AtyrauKAZ/Atyrau5.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AtyrauKAZ/Atyrau6.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)