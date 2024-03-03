
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/HolidaysKAZ/KozheKAZ/Kozhe1.wav", "http://novators.kz/audio/HolidaysKAZ/KozheKAZ/Kozhe2.wav", "http://novators.kz/audio/HolidaysKAZ/KozheKAZ/Kozhe3.wav", "http://novators.kz/audio/HolidaysKAZ/KozheKAZ/Kozhe4.wav", "http://novators.kz/audio/HolidaysKAZ/KozheKAZ/Kozhe5.wav", "http://novators.kz/audio/HolidaysKAZ/KozheKAZ/Kozhe6.wav", "http://novators.kz/audio/HolidaysKAZ/KozheKAZ/Kozhe7.wav", "http://novators.kz/audio/HolidaysKAZ/KozheKAZ/Kozhe8.wav", "http://novators.kz/audio/HolidaysKAZ/KozheKAZ/Kozhe9.wav", "http://novators.kz/audio/HolidaysKAZ/KozheKAZ/Kozhe10.wav", "http://novators.kz/audio/HolidaysKAZ/KozheKAZ/Kozhe11.wav", "http://novators.kz/audio/HolidaysKAZ/KozheKAZ/Kozhe12.wav", "http://novators.kz/audio/HolidaysKAZ/KozheKAZ/Kozhe13.wav", "http://novators.kz/audio/HolidaysKAZ/KozheKAZ/Kozhe14.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
