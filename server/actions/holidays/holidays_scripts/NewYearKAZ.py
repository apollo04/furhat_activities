
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/HolidaysKAZ/NewYearKAZ/NewYear1_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/NewYearKAZ/NewYear2_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/NewYearKAZ/NewYear3_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/NewYearKAZ/NewYear4_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/NewYearKAZ/NewYear5_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/NewYearKAZ/NewYear6_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/NewYearKAZ/NewYear7_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/NewYearKAZ/NewYear8_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/NewYearKAZ/NewYear9_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/NewYearKAZ/NewYear10_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/NewYearKAZ/NewYear11_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/NewYearKAZ/NewYear12_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/NewYearKAZ/NewYear13_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/NewYearKAZ/NewYear14_n.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
