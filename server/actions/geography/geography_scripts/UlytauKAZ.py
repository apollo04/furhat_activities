
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapKAZ/UlytauKAZ/Ulytau1.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/UlytauKAZ/Ulytau2.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/UlytauKAZ/Ulytau3.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/UlytauKAZ/Ulytau4.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/UlytauKAZ/Ulytau5.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/UlytauKAZ/Ulytau6.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
