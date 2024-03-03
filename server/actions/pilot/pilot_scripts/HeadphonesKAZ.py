
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jamie")
    
    url_list = ["http://novators.kz/audio/PilotKAZ/HeadphonesKAZ/HeadphonesKAZ1.wav", "http://novators.kz/audio/PilotKAZ/HeadphonesKAZ/HeadphonesKAZ2.wav", "http://novators.kz/audio/PilotKAZ/HeadphonesKAZ/HeadphonesKAZ3.wav", "http://novators.kz/audio/PilotKAZ/HeadphonesKAZ/HeadphonesKAZ4.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
