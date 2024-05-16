
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/HolidaysKAZ/BirthdayKAZ/Birthday1_n.wav",
                "file:///home/furnix/resources/HolidaysKAZ/BirthdayKAZ/Birthday2_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/BirthdayKAZ/Birthday3_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/BirthdayKAZ/Birthday4_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/BirthdayKAZ/Birthday5_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/BirthdayKAZ/Birthday6_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/BirthdayKAZ/Birthday7_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/BirthdayKAZ/Birthday8_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/BirthdayKAZ/Birthday9_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/BirthdayKAZ/Birthday10_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/BirthdayKAZ/Birthday11_n.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
