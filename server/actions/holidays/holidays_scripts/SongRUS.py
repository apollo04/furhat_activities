
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/HolidaysRUS/SongRUS/SongRUS1_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/SongRUS/SongRUS2_n.wav", 
                "file:///home/furnix/resources/HolidaysRUS/SongRUS/SongRUS3_n.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
    furhat.gesture(name = "BigSmile")
