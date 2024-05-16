
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/HolidaysRUS/NewYearRUS/NewYearRUS1_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/NewYearRUS/NewYearRUS2_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/NewYearRUS/NewYearRUS3_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/NewYearRUS/NewYearRUS4_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/NewYearRUS/NewYearRUS5_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/NewYearRUS/NewYearRUS6_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/NewYearRUS/NewYearRUS7_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/NewYearRUS/NewYearRUS8_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/NewYearRUS/NewYearRUS9_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/NewYearRUS/NewYearRUS10_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/NewYearRUS/NewYearRUS11_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/NewYearRUS/NewYearRUS12_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/NewYearRUS/NewYearRUS13_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/NewYearRUS/NewYearRUS14_n.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
