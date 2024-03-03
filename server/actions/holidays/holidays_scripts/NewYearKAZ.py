
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/HolidaysKAZ/NewYearKAZ/NewYear1.wav", "http://novators.kz/audio/HolidaysKAZ/NewYearKAZ/NewYear2.wav", "http://novators.kz/audio/HolidaysKAZ/NewYearKAZ/NewYear3.wav", "http://novators.kz/audio/HolidaysKAZ/NewYearKAZ/NewYear4.wav", "http://novators.kz/audio/HolidaysKAZ/NewYearKAZ/NewYear5.wav", "http://novators.kz/audio/HolidaysKAZ/NewYearKAZ/NewYear6.wav", "http://novators.kz/audio/HolidaysKAZ/NewYearKAZ/NewYear7.wav", "http://novators.kz/audio/HolidaysKAZ/NewYearKAZ/NewYear8.wav", "http://novators.kz/audio/HolidaysKAZ/NewYearKAZ/NewYear9.wav", "http://novators.kz/audio/HolidaysKAZ/NewYearKAZ/NewYear10.wav", "http://novators.kz/audio/HolidaysKAZ/NewYearKAZ/NewYear11.wav", "http://novators.kz/audio/HolidaysKAZ/NewYearKAZ/NewYear12.wav", "http://novators.kz/audio/HolidaysKAZ/NewYearKAZ/NewYear13.wav", "http://novators.kz/audio/HolidaysKAZ/NewYearKAZ/NewYear14.wav", "http://novators.kz/audio/HolidaysKAZ/NewYearKAZ/NewYear15.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
