
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapRUS/UlytauRUS/Ulytau1.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/UlytauRUS/Ulytau2.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/UlytauRUS/Ulytau3.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/UlytauRUS/Ulytau4.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/UlytauRUS/Ulytau5.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
