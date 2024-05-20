
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/HolidaysRUS/NauryzRUS/NauryzRUS1_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/NauryzRUS/NauryzRUS2_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/NauryzRUS/NauryzRUS3_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/NauryzRUS/NauryzRUS4_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/NauryzRUS/NauryzRUS5_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/NauryzRUS/NauryzRUS6_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/NauryzRUS/NauryzRUS7_n.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
    
