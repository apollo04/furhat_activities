
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jamie")
    
    url_list = ["http://novators.kz/audio/Space/SpaceRUS/VenusRUS/venusRUS1.wav", "http://novators.kz/audio/Space/SpaceRUS/VenusRUS/venusRUS2.wav", "http://novators.kz/audio/Space/SpaceRUS/VenusRUS/endRUS.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
