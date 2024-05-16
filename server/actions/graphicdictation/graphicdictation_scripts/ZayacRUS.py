
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/DictantRUS/ZayacRUS/ZayacRUS1.wav", 
                "file:///home/furnix/resources/DictantRUS/ZayacRUS/ZayacRUS2.wav", 
                "file:///home/furnix/resources/DictantRUS/ZayacRUS/ZayacRUS3.wav", 
                "file:///home/furnix/resources/DictantRUS/ZayacRUS/ZayacRUS4.wav", 
                "file:///home/furnix/resources/DictantRUS/ZayacRUS/ZayacRUS5.wav", 
                "file:///home/furnix/resources/DictantRUS/ZayacRUS/ZayacRUS6.wav", 
                "file:///home/furnix/resources/DictantRUS/ZayacRUS/ZayacRUS7.wav", 
                "file:///home/furnix/resources/DictantRUS/ZayacRUS/ZayacRUS8.wav", 
                "file:///home/furnix/resources/DictantRUS/ZayacRUS/ZayacRUS9.wav", 
                "file:///home/furnix/resources/DictantRUS/ZayacRUS/ZayacRUS10.wav", 
                "file:///home/furnix/resources/DictantRUS/ZayacRUS/ZayacRUS11.wav", 
                "file:///home/furnix/resources/DictantRUS/ZayacRUS/ZayacRUS12.wav", 
                "file:///home/furnix/resources/DictantRUS/ZayacRUS/ZayacRUS13.wav", 
                "file:///home/furnix/resources/DictantRUS/ZayacRUS/ZayacRUS14.wav", 
                "file:///home/furnix/resources/DictantRUS/ZayacRUS/ZayacRUS15.wav", 
                "file:///home/furnix/resources/DictantRUS/ZayacRUS/ZayacRUS16.wav", 
                "file:///home/furnix/resources/DictantRUS/ZayacRUS/ZayacRUS17.wav", 
                "file:///home/furnix/resources/DictantRUS/ZayacRUS/ZayacRUS18.wav", 
                "file:///home/furnix/resources/DictantRUS/ZayacRUS/ZayacRUS19.wav", 
                "file:///home/furnix/resources/DictantRUS/ZayacRUS/ZayacRUS20.wav", 
                "file:///home/furnix/resources/DictantRUS/ZayacRUS/ZayacRUS21.wav", 
                "file:///home/furnix/resources/DictantRUS/ZayacRUS/ZayacRUS22.wav", 
                "file:///home/furnix/resources/DictantRUS/ZayacRUS/ZayacRUS23.wav", 
                "file:///home/furnix/resources/DictantRUS/ZayacRUS/ZayacRUS24.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
