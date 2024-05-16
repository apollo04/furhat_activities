
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Alex")
    
    url_list = ["file:///home/furnix/resources/SuperheroesKAZ/IronmanKAZ/Ironman1.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/IronmanKAZ/Ironman2.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/IronmanKAZ/Ironman3.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/IronmanKAZ/Ironman4.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/IronmanKAZ/Ironman5.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/IronmanKAZ/Ironman6.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/IronmanKAZ/Ironman7.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/IronmanKAZ/Ironman8.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/IronmanKAZ/Ironman9.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/IronmanKAZ/Ironman10.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/IronmanKAZ/Ironman11.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
