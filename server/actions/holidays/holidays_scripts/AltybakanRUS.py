
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/HolidaysRUS/AltybakanRUS/AltybakanRUS1.wav", "http://novators.kz/audio/HolidaysRUS/AltybakanRUS/AltybakanRUS2.wav", "http://novators.kz/audio/HolidaysRUS/AltybakanRUS/AltybakanRUS3.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
