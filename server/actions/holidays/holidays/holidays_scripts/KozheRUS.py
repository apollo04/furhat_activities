
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/HolidaysRUS/KozheRUS/KozheRUS1_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/KozheRUS/KozheRUS2_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/KozheRUS/KozheRUS3_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/KozheRUS/KozheRUS4_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/KozheRUS/KozheRUS5_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/KozheRUS/KozheRUS6_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/KozheRUS/KozheRUS7_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/KozheRUS/KozheRUS8_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/KozheRUS/KozheRUS9_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/KozheRUS/KozheRUS10_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/KozheRUS/KozheRUS11_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/KozheRUS/KozheRUS12_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/KozheRUS/KozheRUS13_n.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
