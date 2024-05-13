
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Omar")
    
    url_list = ["file:///home/furnix/resources/FirefighterRUS/FirefighterCarRUS/FirefighterCarRUS1.wav", 
                "file:///home/furnix/resources/FirefighterRUS/FirefighterCarRUS/FirefighterCarRUS2.wav", 
                "file:///home/furnix/resources/FirefighterRUS/FirefighterCarRUS/FirefighterCarRUS3.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
