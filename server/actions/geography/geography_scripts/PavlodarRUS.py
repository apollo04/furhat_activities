
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapRUS/PavlodarRUS/Pavlodar1.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/PavlodarRUS/Pavlodar2.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/PavlodarRUS/Pavlodar3.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/PavlodarRUS/Pavlodar4.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/PavlodarRUS/Pavlodar5.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/PavlodarRUS/Pavlodar6.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
