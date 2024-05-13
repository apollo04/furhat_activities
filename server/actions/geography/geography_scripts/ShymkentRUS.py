
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapRUS/ShymkentRUS/Shymkent1.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/ShymkentRUS/Shymkent2.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/ShymkentRUS/Shymkent3.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/ShymkentRUS/Shymkent4.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)