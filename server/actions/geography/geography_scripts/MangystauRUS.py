
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapRUS/MangystauRUS/Mangystau1.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/MangystauRUS/Mangystau2.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/MangystauRUS/Mangystau3.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/MangystauRUS/Mangystau4.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/MangystauRUS/Mangystau5.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/MangystauRUS/Mangystau6.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/MangystauRUS/Mangystau7.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/MangystauRUS/Mangystau8.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
