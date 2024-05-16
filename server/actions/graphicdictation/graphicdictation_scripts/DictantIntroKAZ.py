
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/DictantKAZ/IntroKAZ/IntroKAZ1.wav", 
                "file:///home/furnix/resources/DictantKAZ/IntroKAZ/IntroKAZ2.wav", 
                "file:///home/furnix/resources/DictantKAZ/IntroKAZ/IntroKAZ3.wav", 
                "file:///home/furnix/resources/DictantKAZ/IntroKAZ/IntroKAZ4.wav", 
                "file:///home/furnix/resources/DictantKAZ/IntroKAZ/IntroKAZ5.wav", 
                "file:///home/furnix/resources/DictantKAZ/IntroKAZ/IntroKAZ6.wav", 
                "file:///home/furnix/resources/DictantKAZ/IntroKAZ/IntroKAZ7.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
