
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapRUS/KyzylordaRUS/Kyzylorda1.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/KyzylordaRUS/Kyzylorda2.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/KyzylordaRUS/Kyzylorda3.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/KyzylordaRUS/Kyzylorda4.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/KyzylordaRUS/Kyzylorda5.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
