
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Omar")
    
    url_list = ["file:///home/furnix/resources/FirefighterKAZ/FirefighterInfoKAZ/FirefighterInfoKAZ1.wav", 
                "file:///home/furnix/resources/FirefighterKAZ/FirefighterInfoKAZ/FirefighterInfoKAZ2.wav", 
                "file:///home/furnix/resources/FirefighterKAZ/FirefighterInfoKAZ/FirefighterInfoKAZ3.wav", 
                "file:///home/furnix/resources/FirefighterKAZ/FirefighterInfoKAZ/FirefighterInfoKAZ4.wav", 
                "file:///home/furnix/resources/FirefighterKAZ/FirefighterInfoKAZ/FirefighterInfoKAZ5.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
