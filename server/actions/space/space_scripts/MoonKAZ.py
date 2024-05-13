
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="James")
    
    url_list = ["file:///home/furnix/resources/Space/SpaceKAZ/MoonKAZ/moonKAZ1.wav", 
                "file:///home/furnix/resources/Space/SpaceKAZ/MoonKAZ/moonKAZ2.wav", 
                "file:///home/furnix/resources/Space/SpaceKAZ/MoonKAZ/endKAZ.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
