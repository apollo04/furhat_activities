
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/DictantRUS/KeyRUS/Key1.wav", 
                "file:///home/furnix/resources/DictantRUS/KeyRUS/Key2.wav", 
                "file:///home/furnix/resources/DictantRUS/KeyRUS/Key3.wav", 
                "file:///home/furnix/resources/DictantRUS/KeyRUS/Key4.wav", 
                "file:///home/furnix/resources/DictantRUS/KeyRUS/Key5.wav", 
                "file:///home/furnix/resources/DictantRUS/KeyRUS/Key6.wav", 
                "file:///home/furnix/resources/DictantRUS/KeyRUS/Key7.wav", 
                "file:///home/furnix/resources/DictantRUS/KeyRUS/Key8.wav", 
                "file:///home/furnix/resources/DictantRUS/KeyRUS/Key9.wav", 
                "file:///home/furnix/resources/DictantRUS/KeyRUS/Key10.wav", 
                "file:///home/furnix/resources/DictantRUS/KeyRUS/Key11.wav", 
                "file:///home/furnix/resources/DictantRUS/KeyRUS/Key12.wav", 
                "file:///home/furnix/resources/DictantRUS/KeyRUS/Key13.wav", 
                "file:///home/furnix/resources/DictantRUS/KeyRUS/Key14.wav", 
                "file:///home/furnix/resources/DictantRUS/KeyRUS/Key15.wav", 
                "file:///home/furnix/resources/DictantRUS/KeyRUS/Key16.wav", 
                "file:///home/furnix/resources/DictantRUS/KeyRUS/Key17.wav", 
                "file:///home/furnix/resources/DictantRUS/KeyRUS/Key18.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
