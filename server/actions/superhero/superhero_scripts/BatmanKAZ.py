
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Alex")
    
    url_list = ["file:///home/furnix/resources/SuperheroesKAZ/BatmanKAZ/Batman1.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/BatmanKAZ/Batman2.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/BatmanKAZ/Batman3.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/BatmanKAZ/Batman4.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/BatmanKAZ/Batman5.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/BatmanKAZ/Batman6.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/BatmanKAZ/Batman7.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/BatmanKAZ/Batman8.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/BatmanKAZ/Batman9.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/BatmanKAZ/Batman10.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
