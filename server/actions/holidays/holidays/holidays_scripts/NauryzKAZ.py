
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/HolidaysKAZ/NauryzKAZ/Nauryz1_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/NauryzKAZ/Nauryz2_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/NauryzKAZ/Nauryz3_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/NauryzKAZ/Nauryz4_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/NauryzKAZ/Nauryz5_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/NauryzKAZ/Nauryz6_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/NauryzKAZ/Nauryz7_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/NauryzKAZ/Nauryz8_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/NauryzKAZ/Nauryz9_n.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
