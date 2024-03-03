
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Alex")
    
    url_list = ["http://novators.kz/audio/SuperheroesKAZ/BatmanKAZ/Batman1.wav", "http://novators.kz/audio/SuperheroesKAZ/BatmanKAZ/Batman2.wav", "http://novators.kz/audio/SuperheroesKAZ/BatmanKAZ/Batman3.wav", "http://novators.kz/audio/SuperheroesKAZ/BatmanKAZ/Batman4.wav", "http://novators.kz/audio/SuperheroesKAZ/BatmanKAZ/Batman5.wav", "http://novators.kz/audio/SuperheroesKAZ/BatmanKAZ/Batman6.wav", "http://novators.kz/audio/SuperheroesKAZ/BatmanKAZ/Batman7.wav", "http://novators.kz/audio/SuperheroesKAZ/BatmanKAZ/Batman8.wav", "http://novators.kz/audio/SuperheroesKAZ/BatmanKAZ/Batman9.wav", "http://novators.kz/audio/SuperheroesKAZ/BatmanKAZ/Batman10.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
