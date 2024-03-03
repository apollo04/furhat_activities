
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Alex")
    
    url_list = ["http://novators.kz/audio/SuperheroesRUS/BatmanRUS/Batman1.wav", "http://novators.kz/audio/SuperheroesRUS/BatmanRUS/Batman2.wav", "http://novators.kz/audio/SuperheroesRUS/BatmanRUS/Batman3.wav", "http://novators.kz/audio/SuperheroesRUS/BatmanRUS/Batman4.wav", "http://novators.kz/audio/SuperheroesRUS/BatmanRUS/Batman5.wav", "http://novators.kz/audio/SuperheroesRUS/BatmanRUS/Batman6.wav", "http://novators.kz/audio/SuperheroesRUS/BatmanRUS/Batman7.wav", "http://novators.kz/audio/SuperheroesRUS/BatmanRUS/Batman8.wav", "http://novators.kz/audio/SuperheroesRUS/BatmanRUS/Batman9.wav", "http://novators.kz/audio/SuperheroesRUS/BatmanRUS/Batman10.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
