
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Alex")
    
    url_list = ["http://novators.kz/audio/SuperheroesKAZ/IronmanKAZ/Ironman1.wav", "http://novators.kz/audio/SuperheroesKAZ/IronmanKAZ/Ironman2.wav", "http://novators.kz/audio/SuperheroesKAZ/IronmanKAZ/Ironman3.wav", "http://novators.kz/audio/SuperheroesKAZ/IronmanKAZ/Ironman4.wav", "http://novators.kz/audio/SuperheroesKAZ/IronmanKAZ/Ironman5.wav", "http://novators.kz/audio/SuperheroesKAZ/IronmanKAZ/Ironman6.wav", "http://novators.kz/audio/SuperheroesKAZ/IronmanKAZ/Ironman7.wav", "http://novators.kz/audio/SuperheroesKAZ/IronmanKAZ/Ironman8.wav", "http://novators.kz/audio/SuperheroesKAZ/IronmanKAZ/Ironman9.wav", "http://novators.kz/audio/SuperheroesKAZ/IronmanKAZ/Ironman10.wav", "http://novators.kz/audio/SuperheroesKAZ/IronmanKAZ/Ironman11.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
