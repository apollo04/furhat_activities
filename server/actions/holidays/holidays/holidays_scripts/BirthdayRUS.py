
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/HolidaysRUS/BirthdayRUS/BirthdayRUS1_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/BirthdayRUS/BirthdayRUS2_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/BirthdayRUS/BirthdayRUS3_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/BirthdayRUS/BirthdayRUS4_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/BirthdayRUS/BirthdayRUS5_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/BirthdayRUS/BirthdayRUS6_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/BirthdayRUS/BirthdayRUS7_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/BirthdayRUS/BirthdayRUS8_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/BirthdayRUS/BirthdayRUS9_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/BirthdayRUS/BirthdayRUS10_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/BirthdayRUS/BirthdayRUS11_n.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
