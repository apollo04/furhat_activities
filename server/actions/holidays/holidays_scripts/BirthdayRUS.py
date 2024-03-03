
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/HolidaysRUS/BirthdayRUS/BirthdayRUS1.wav", "http://novators.kz/audio/HolidaysRUS/BirthdayRUS/BirthdayRUS2.wav", "http://novators.kz/audio/HolidaysRUS/BirthdayRUS/BirthdayRUS3.wav", "http://novators.kz/audio/HolidaysRUS/BirthdayRUS/BirthdayRUS4.wav", "http://novators.kz/audio/HolidaysRUS/BirthdayRUS/BirthdayRUS5.wav", "http://novators.kz/audio/HolidaysRUS/BirthdayRUS/BirthdayRUS6.wav", "http://novators.kz/audio/HolidaysRUS/BirthdayRUS/BirthdayRUS7.wav", "http://novators.kz/audio/HolidaysRUS/BirthdayRUS/BirthdayRUS8.wav", "http://novators.kz/audio/HolidaysRUS/BirthdayRUS/BirthdayRUS9.wav", "http://novators.kz/audio/HolidaysRUS/BirthdayRUS/BirthdayRUS10.wav", "http://novators.kz/audio/HolidaysRUS/BirthdayRUS/BirthdayRUS11.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
