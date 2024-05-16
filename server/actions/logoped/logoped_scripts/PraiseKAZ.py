
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Isabel")
    
    url_list = ["file:///home/furnix/resources/LogopedKAZ/PraiseKAZ/PraiseKAZ1.wav", 
                "file:///home/furnix/resources/LogopedKAZ/PraiseKAZ/PraiseKAZ2.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
