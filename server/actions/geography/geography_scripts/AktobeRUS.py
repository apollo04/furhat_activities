
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapRUS/AktobeRUS/Aktobe1.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AktobeRUS/Aktobe2.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AktobeRUS/Aktobe3.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AktobeRUS/Aktobe4.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AktobeRUS/Aktobe5.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AktobeRUS/Aktobe6.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
