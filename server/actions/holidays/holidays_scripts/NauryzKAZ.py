
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/HolidaysKAZ/NauryzKAZ/Nauryz1.wav", "http://novators.kz/audio/HolidaysKAZ/NauryzKAZ/Nauryz2.wav", "http://novators.kz/audio/HolidaysKAZ/NauryzKAZ/Nauryz3.wav", "http://novators.kz/audio/HolidaysKAZ/NauryzKAZ/Nauryz4.wav", "http://novators.kz/audio/HolidaysKAZ/NauryzKAZ/Nauryz5.wav", "http://novators.kz/audio/HolidaysKAZ/NauryzKAZ/Nauryz6.wav", "http://novators.kz/audio/HolidaysKAZ/NauryzKAZ/Nauryz7.wav", "http://novators.kz/audio/HolidaysKAZ/NauryzKAZ/Nauryz8.wav", "http://novators.kz/audio/HolidaysKAZ/NauryzKAZ/Nauryz9.wav", "http://novators.kz/audio/HolidaysKAZ/NauryzKAZ/Nauryz10.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
