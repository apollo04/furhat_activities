
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapKAZ/PavlodarKAZ/Pavlodar1.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/PavlodarKAZ/Pavlodar2.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/PavlodarKAZ/Pavlodar3.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/PavlodarKAZ/Pavlodar4.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/PavlodarKAZ/Pavlodar5.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/PavlodarKAZ/Pavlodar6.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
