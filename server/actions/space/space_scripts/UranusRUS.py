
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jamie")
    
    url_list = ["http://novators.kz/audio/Space/SpaceRUS/UranusRUS/uranusRUS1.wav", "http://novators.kz/audio/Space/SpaceRUS/UranusRUS/uranusRUS2.wav", "http://novators.kz/audio/Space/SpaceRUS/UranusRUS/endRUS.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
