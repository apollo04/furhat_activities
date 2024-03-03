
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/HolidaysKAZ/SongKAZ/Song1.wav", "http://novators.kz/audio/HolidaysKAZ/SongKAZ/Song2.wav", "http://novators.kz/audio/HolidaysKAZ/SongKAZ/Song3.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
