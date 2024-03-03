
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/HolidaysRUS/NewYearRUS/NewYearRUS1.wav", "http://novators.kz/audio/HolidaysRUS/NewYearRUS/NewYearRUS2.wav", "http://novators.kz/audio/HolidaysRUS/NewYearRUS/NewYearRUS3.wav", "http://novators.kz/audio/HolidaysRUS/NewYearRUS/NewYearRUS4.wav", "http://novators.kz/audio/HolidaysRUS/NewYearRUS/NewYearRUS5.wav", "http://novators.kz/audio/HolidaysRUS/NewYearRUS/NewYearRUS6.wav", "http://novators.kz/audio/HolidaysRUS/NewYearRUS/NewYearRUS7.wav", "http://novators.kz/audio/HolidaysRUS/NewYearRUS/NewYearRUS8.wav", "http://novators.kz/audio/HolidaysRUS/NewYearRUS/NewYearRUS9.wav", "http://novators.kz/audio/HolidaysRUS/NewYearRUS/NewYearRUS10.wav", "http://novators.kz/audio/HolidaysRUS/NewYearRUS/NewYearRUS11.wav", "http://novators.kz/audio/HolidaysRUS/NewYearRUS/NewYearRUS12.wav", "http://novators.kz/audio/HolidaysRUS/NewYearRUS/NewYearRUS13.wav", "http://novators.kz/audio/HolidaysRUS/NewYearRUS/NewYearRUS14.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
