
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Alex")
    
    url_list = ["http://novators.kz/audio/SuperheroesKAZ/CaptainAmericaKAZ/CaptainAmericaKAZ1.wav",
                "http://novators.kz/audio/SuperheroesKAZ/CaptainAmericaKAZ/CaptainAmericaKAZ2.wav", 
                "http://novators.kz/audio/SuperheroesKAZ/CaptainAmericaKAZ/CaptainAmericaKAZ3.wav", 
                "http://novators.kz/audio/SuperheroesKAZ/CaptainAmericaKAZ/CaptainAmericaKAZ4.wav", 
                "http://novators.kz/audio/SuperheroesKAZ/CaptainAmericaKAZ/CaptainAmericaKAZ5.wav", 
                "http://novators.kz/audio/SuperheroesKAZ/CaptainAmericaKAZ/CaptainAmericaKAZ6.wav", 
                "http://novators.kz/audio/SuperheroesKAZ/CaptainAmericaKAZ/CaptainAmericaKAZ7.wav", 
                "http://novators.kz/audio/SuperheroesKAZ/CaptainAmericaKAZ/CaptainAmericaKAZ8.wav", 
                "http://novators.kz/audio/SuperheroesKAZ/CaptainAmericaKAZ/CaptainAmericaKAZ9.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)