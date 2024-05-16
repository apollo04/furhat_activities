
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/DictantRUS/ElephantRUS/ElephantRUS1.wav", 
                "file:///home/furnix/resources/DictantRUS/ElephantRUS/ElephantRUS2.wav", 
                "file:///home/furnix/resources/DictantRUS/ElephantRUS/ElephantRUS3.wav", 
                "file:///home/furnix/resources/DictantRUS/ElephantRUS/ElephantRUS4.wav", 
                "file:///home/furnix/resources/DictantRUS/ElephantRUS/ElephantRUS5.wav", 
                "file:///home/furnix/resources/DictantRUS/ElephantRUS/ElephantRUS6.wav", 
                "file:///home/furnix/resources/DictantRUS/ElephantRUS/ElephantRUS7.wav", 
                "file:///home/furnix/resources/DictantRUS/ElephantRUS/ElephantRUS8.wav", 
                "file:///home/furnix/resources/DictantRUS/ElephantRUS/ElephantRUS9.wav", 
                "file:///home/furnix/resources/DictantRUS/ElephantRUS/ElephantRUS10.wav", 
                "file:///home/furnix/resources/DictantRUS/ElephantRUS/ElephantRUS11.wav", 
                "file:///home/furnix/resources/DictantRUS/ElephantRUS/ElephantRUS12.wav", 
                "file:///home/furnix/resources/DictantRUS/ElephantRUS/ElephantRUS13.wav", 
                "file:///home/furnix/resources/DictantRUS/ElephantRUS/ElephantRUS14.wav", 
                "file:///home/furnix/resources/DictantRUS/ElephantRUS/ElephantRUS15.wav", 
                "file:///home/furnix/resources/DictantRUS/ElephantRUS/ElephantRUS16.wav", 
                "file:///home/furnix/resources/DictantRUS/ElephantRUS/ElephantRUS17.wav", 
                "file:///home/furnix/resources/DictantRUS/ElephantRUS/ElephantRUS18.wav", 
                "file:///home/furnix/resources/DictantRUS/ElephantRUS/ElephantRUS19.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
