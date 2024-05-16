
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/HolidaysRUS/HolidaysRUS1_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/HolidaysRUS2_n.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
