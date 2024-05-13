
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapKAZ/MangystauKAZ/Mangystau1.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/MangystauKAZ/Mangystau2.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/MangystauKAZ/Mangystau3.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/MangystauKAZ/Mangystau4.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/MangystauKAZ/Mangystau5.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/MangystauKAZ/Mangystau6.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/MangystauKAZ/Mangystau7.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/MangystauKAZ/Mangystau8.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
