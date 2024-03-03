
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/KazakhstanMapRUS/PavlodarRUS/Pavlodar1.wav", "http://novators.kz/audio/KazakhstanMapRUS/PavlodarRUS/Pavlodar2.wav", "http://novators.kz/audio/KazakhstanMapRUS/PavlodarRUS/Pavlodar3.wav", "http://novators.kz/audio/KazakhstanMapRUS/PavlodarRUS/Pavlodar4.wav", "http://novators.kz/audio/KazakhstanMapRUS/PavlodarRUS/Pavlodar5.wav", "http://novators.kz/audio/KazakhstanMapRUS/PavlodarRUS/Pavlodar6.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
