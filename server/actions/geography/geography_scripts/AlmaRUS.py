
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapRUS/AlmaRUS/Alma1.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AlmaRUS/Alma2.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AlmaRUS/Alma3.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AlmaRUS/Alma4.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AlmaRUS/Alma5.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AlmaRUS/Alma6.wav",
                "file:///home/furnix/resources/KazakhstanMapRUS/AlmaRUS/Alma7.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)