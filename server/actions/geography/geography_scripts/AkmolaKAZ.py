
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapKAZ/AkmolaKAZ/Akmola1.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AkmolaKAZ/Akmola2.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AkmolaKAZ/Akmola3.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AkmolaKAZ/Akmola4.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AkmolaKAZ/Akmola5.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AkmolaKAZ/Akmola6.wav",
                "file:///home/furnix/resources/KazakhstanMapKAZ/AkmolaKAZ/Akmola7.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)