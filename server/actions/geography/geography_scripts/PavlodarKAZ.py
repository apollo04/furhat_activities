
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/KazakhstanMapKAZ/PavlodarKAZ/Pavlodar1.wav", "http://novators.kz/audio/KazakhstanMapKAZ/PavlodarKAZ/Pavlodar2.wav", "http://novators.kz/audio/KazakhstanMapKAZ/PavlodarKAZ/Pavlodar3.wav", "http://novators.kz/audio/KazakhstanMapKAZ/PavlodarKAZ/Pavlodar4.wav", "http://novators.kz/audio/KazakhstanMapKAZ/PavlodarKAZ/Pavlodar5.wav", "http://novators.kz/audio/KazakhstanMapKAZ/PavlodarKAZ/Pavlodar6.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
