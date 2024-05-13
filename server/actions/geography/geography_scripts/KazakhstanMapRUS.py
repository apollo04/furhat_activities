
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapRUS/APP1.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/APP2.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/APP3.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/APP4.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/APP5.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/APP6.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/APP7.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/APP8.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/APP9.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/APP10.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
