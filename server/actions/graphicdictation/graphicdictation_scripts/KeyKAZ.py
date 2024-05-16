
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/DictantKAZ/KeyKAZ/Key1.wav", 
                "file:///home/furnix/resources/DictantKAZ/KeyKAZ/Key2.wav", 
                "file:///home/furnix/resources/DictantKAZ/KeyKAZ/Key3.wav", 
                "file:///home/furnix/resources/DictantKAZ/KeyKAZ/Key4.wav", 
                "file:///home/furnix/resources/DictantKAZ/KeyKAZ/Key5.wav", 
                "file:///home/furnix/resources/DictantKAZ/KeyKAZ/Key6.wav", 
                "file:///home/furnix/resources/DictantKAZ/KeyKAZ/Key7.wav", 
                "file:///home/furnix/resources/DictantKAZ/KeyKAZ/Key8.wav", 
                "file:///home/furnix/resources/DictantKAZ/KeyKAZ/Key9.wav", 
                "file:///home/furnix/resources/DictantKAZ/KeyKAZ/Key10.wav", 
                "file:///home/furnix/resources/DictantKAZ/KeyKAZ/Key11.wav", 
                "file:///home/furnix/resources/DictantKAZ/KeyKAZ/Key12.wav", 
                "file:///home/furnix/resources/DictantKAZ/KeyKAZ/Key13.wav", 
                "file:///home/furnix/resources/DictantKAZ/KeyKAZ/Key14.wav", 
                "file:///home/furnix/resources/DictantKAZ/KeyKAZ/Key15.wav", 
                "file:///home/furnix/resources/DictantKAZ/KeyKAZ/Key16.wav", 
                "file:///home/furnix/resources/DictantKAZ/KeyKAZ/Key17.wav", 
                "file:///home/furnix/resources/DictantKAZ/KeyKAZ/Key18.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
