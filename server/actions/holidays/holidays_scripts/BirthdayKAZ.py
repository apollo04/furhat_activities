
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/HolidaysKAZ/BirthdayKAZ/Birthday1.wav", "http://novators.kz/audio/HolidaysKAZ/BirthdayKAZ/Birthday2.wav", "http://novators.kz/audio/HolidaysKAZ/BirthdayKAZ/Birthday3.wav", "http://novators.kz/audio/HolidaysKAZ/BirthdayKAZ/Birthday4.wav", "http://novators.kz/audio/HolidaysKAZ/BirthdayKAZ/Birthday5.wav", "http://novators.kz/audio/HolidaysKAZ/BirthdayKAZ/Birthday6.wav", "http://novators.kz/audio/HolidaysKAZ/BirthdayKAZ/Birthday7.wav", "http://novators.kz/audio/HolidaysKAZ/BirthdayKAZ/Birthday8.wav", "http://novators.kz/audio/HolidaysKAZ/BirthdayKAZ/Birthday9.wav", "http://novators.kz/audio/HolidaysKAZ/BirthdayKAZ/Birthday10.wav", "http://novators.kz/audio/HolidaysKAZ/BirthdayKAZ/Birthday11.wav", "http://novators.kz/audio/HolidaysKAZ/BirthdayKAZ/Birthday12.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
