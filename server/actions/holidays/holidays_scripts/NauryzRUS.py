
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/HolidaysRUS/NauryzRUS/NauryzRUS1.wav", "http://novators.kz/audio/HolidaysRUS/NauryzRUS/NauryzRUS2.wav", "http://novators.kz/audio/HolidaysRUS/NauryzRUS/NauryzRUS3.wav", "http://novators.kz/audio/HolidaysRUS/NauryzRUS/NauryzRUS4.wav", "http://novators.kz/audio/HolidaysRUS/NauryzRUS/NauryzRUS5.wav", "http://novators.kz/audio/HolidaysRUS/NauryzRUS/NauryzRUS6.wav", "http://novators.kz/audio/HolidaysRUS/NauryzRUS/NauryzRUS7.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
