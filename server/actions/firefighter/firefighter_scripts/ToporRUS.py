
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Omar")
    
    url_list = ["http://novators.kz/audio/FirefighterRUS/ToporRUS/ToporRUS1.wav", "http://novators.kz/audio/FirefighterRUS/ToporRUS/ToporRUS2.wav", "http://novators.kz/audio/FirefighterRUS/ToporRUS/ToporRUS3.wav", "http://novators.kz/audio/FirefighterRUS/ToporRUS/ToporRUS4.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
