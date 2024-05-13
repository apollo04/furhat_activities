
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapKAZ/APP1.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/APP2.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/APP3.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/APP4.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/APP5.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/APP6.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/APP7.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/APP8.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/APP9.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/APP10.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
