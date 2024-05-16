
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Alex")
    
    url_list = ["file:///home/furnix/resources/SuperheroesKAZ/CaptainAmericaKAZ/CaptainAmericaKAZ1.wav",
                "file:///home/furnix/resources/SuperheroesKAZ/CaptainAmericaKAZ/CaptainAmericaKAZ2.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/CaptainAmericaKAZ/CaptainAmericaKAZ3.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/CaptainAmericaKAZ/CaptainAmericaKAZ4.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/CaptainAmericaKAZ/CaptainAmericaKAZ5.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/CaptainAmericaKAZ/CaptainAmericaKAZ6.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/CaptainAmericaKAZ/CaptainAmericaKAZ7.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/CaptainAmericaKAZ/CaptainAmericaKAZ8.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/CaptainAmericaKAZ/CaptainAmericaKAZ9.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)