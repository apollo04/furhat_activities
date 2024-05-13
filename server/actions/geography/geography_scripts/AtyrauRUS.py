
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapRUS/AtyrauRUS/Atyrau1.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AtyrauRUS/Atyrau2.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AtyrauRUS/Atyrau3.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AtyrauRUS/Atyrau4.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AtyrauRUS/Atyrau5.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AtyrauRUS/Atyrau6.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)