
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapKAZ/KyzylordaKAZ/Kyzylorda1.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/KyzylordaKAZ/Kyzylorda2.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/KyzylordaKAZ/Kyzylorda3.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/KyzylordaKAZ/Kyzylorda4.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/KyzylordaKAZ/Kyzylorda5.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/KyzylordaKAZ/Kyzylorda6.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
