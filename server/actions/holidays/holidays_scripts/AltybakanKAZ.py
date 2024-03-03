
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/HolidaysKAZ/AltybakanKAZ/Altybakan1.wav", "http://novators.kz/audio/HolidaysKAZ/AltybakanKAZ/Altybakan2.wav", "http://novators.kz/audio/HolidaysKAZ/AltybakanKAZ/Altybakan3.wav", "http://novators.kz/audio/HolidaysKAZ/AltybakanKAZ/Altybakan4.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
