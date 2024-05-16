
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Alex")
    
    url_list = ["file:///home/furnix/resources/SuperheroesRUS/BatmanRUS/Batman1.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/BatmanRUS/Batman2.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/BatmanRUS/Batman3.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/BatmanRUS/Batman4.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/BatmanRUS/Batman5.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/BatmanRUS/Batman6.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/BatmanRUS/Batman7.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/BatmanRUS/Batman8.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/BatmanRUS/Batman9.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/BatmanRUS/Batman10.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
