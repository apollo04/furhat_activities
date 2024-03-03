
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/HolidaysRUS/KozheRUS/KozheRUS1.wav", "http://novators.kz/audio/HolidaysRUS/KozheRUS/KozheRUS2.wav", "http://novators.kz/audio/HolidaysRUS/KozheRUS/KozheRUS3.wav", "http://novators.kz/audio/HolidaysRUS/KozheRUS/KozheRUS4.wav", "http://novators.kz/audio/HolidaysRUS/KozheRUS/KozheRUS5.wav", "http://novators.kz/audio/HolidaysRUS/KozheRUS/KozheRUS6.wav", "http://novators.kz/audio/HolidaysRUS/KozheRUS/KozheRUS7.wav", "http://novators.kz/audio/HolidaysRUS/KozheRUS/KozheRUS8.wav", "http://novators.kz/audio/HolidaysRUS/KozheRUS/KozheRUS9.wav", "http://novators.kz/audio/HolidaysRUS/KozheRUS/KozheRUS10.wav", "http://novators.kz/audio/HolidaysRUS/KozheRUS/KozheRUS11.wav", "http://novators.kz/audio/HolidaysRUS/KozheRUS/KozheRUS12.wav", "http://novators.kz/audio/HolidaysRUS/KozheRUS/KozheRUS13.wav", "http://novators.kz/audio/HolidaysRUS/KozheRUS/KozheRUS14.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
