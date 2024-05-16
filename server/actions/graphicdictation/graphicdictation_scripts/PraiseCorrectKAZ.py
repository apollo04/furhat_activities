
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/DictantKAZ/PraiseCorrectKAZ/PraiseKAZ1.wav", 
                "file:///home/furnix/resources/DictantKAZ/PraiseCorrectKAZ/PraiseKAZ2.wav", 
                "file:///home/furnix/resources/DictantKAZ/PraiseCorrectKAZ/PraiseKAZ3.wav", 
                "file:///home/furnix/resources/DictantKAZ/PraiseCorrectKAZ/PraiseKAZ4.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
