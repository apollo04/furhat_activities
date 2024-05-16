
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Alex")
    
    url_list = ["file:///home/furnix/resources/SuperheroesKAZ/IntroKAZ/IntroKAZ1.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/IntroKAZ/IntroKAZ2.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/IntroKAZ/IntroKAZ3.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/IntroKAZ/IntroKAZ4.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
