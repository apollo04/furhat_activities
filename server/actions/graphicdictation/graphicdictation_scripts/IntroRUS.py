
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/DictantRUS/IntroRUS/IntroRUS1.wav", 
                "file:///home/furnix/resources/DictantRUS/IntroRUS/IntroRUS2.wav", 
                "file:///home/furnix/resources/DictantRUS/IntroRUS/IntroRUS3.wav", 
                "file:///home/furnix/resources/DictantRUS/IntroRUS/IntroRUS4.wav", 
                "file:///home/furnix/resources/DictantRUS/IntroRUS/IntroRUS5.wav", 
                "file:///home/furnix/resources/DictantRUS/IntroRUS/IntroRUS6.wav", 
                "file:///home/furnix/resources/DictantRUS/IntroRUS/IntroRUS7.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
