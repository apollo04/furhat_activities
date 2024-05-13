
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Omar")
    
    url_list = ["file:///home/furnix/resources/FirefighterKAZ/PraiseCorrectKAZ/profPraiseKAZ1.wav", 
                "file:///home/furnix/resources/FirefighterKAZ/PraiseCorrectKAZ/profPraiseKAZ2.wav", 
                "file:///home/furnix/resources/FirefighterKAZ/PraiseCorrectKAZ/profPraiseKAZ3.wav", 
                "file:///home/furnix/resources/FirefighterKAZ/PraiseCorrectKAZ/profPraiseKAZ4.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
