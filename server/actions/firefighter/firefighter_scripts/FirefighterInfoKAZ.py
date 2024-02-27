
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Omar")
    
    url_list = ["http://novators.kz/audio/FirefighterKAZ/FirefighterInfoKAZ/FirefighterInfoKAZ1.wav", "http://novators.kz/audio/FirefighterKAZ/FirefighterInfoKAZ/FirefighterInfoKAZ2.wav", "http://novators.kz/audio/FirefighterKAZ/FirefighterInfoKAZ/FirefighterInfoKAZ3.wav", "http://novators.kz/audio/FirefighterKAZ/FirefighterInfoKAZ/FirefighterInfoKAZ4.wav", "http://novators.kz/audio/FirefighterKAZ/FirefighterInfoKAZ/FirefighterInfoKAZ5.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
