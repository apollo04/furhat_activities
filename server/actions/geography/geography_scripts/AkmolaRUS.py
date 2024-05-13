
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapRUS/AkmolaRUS/Akmola1.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AkmolaRUS/Akmola2.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AkmolaRUS/Akmola3.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AkmolaRUS/Akmola4.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AkmolaRUS/Akmola5.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AkmolaRUS/Akmola6.wav",
                "file:///home/furnix/resources/KazakhstanMapRUS/AkmolaRUS/Akmola7.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)