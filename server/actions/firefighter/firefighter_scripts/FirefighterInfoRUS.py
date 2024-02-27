
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Omar")
    
    url_list = ["http://novators.kz/audio/FirefighterRUS/FirefighterInfoRUS/FirefighterInfoRUS1.wav", "http://novators.kz/audio/FirefighterRUS/FirefighterInfoRUS/FirefighterInfoRUS2.wav", "http://novators.kz/audio/FirefighterRUS/FirefighterInfoRUS/FirefighterInfoRUS3.wav", "http://novators.kz/audio/FirefighterRUS/FirefighterInfoRUS/FirefighterInfoRUS4.wav", "http://novators.kz/audio/FirefighterRUS/FirefighterInfoRUS/FirefighterInfoRUS5.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
