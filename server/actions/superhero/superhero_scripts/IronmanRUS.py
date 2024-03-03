
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Alex")
    
    url_list = ["http://novators.kz/audio/SuperheroesRUS/IronmanRUS/Ironman1.wav", "http://novators.kz/audio/SuperheroesRUS/IronmanRUS/Ironman2.wav", "http://novators.kz/audio/SuperheroesRUS/IronmanRUS/Ironman3.wav", "http://novators.kz/audio/SuperheroesRUS/IronmanRUS/Ironman4.wav", "http://novators.kz/audio/SuperheroesRUS/IronmanRUS/Ironman5.wav", "http://novators.kz/audio/SuperheroesRUS/IronmanRUS/Ironman6.wav", "http://novators.kz/audio/SuperheroesRUS/IronmanRUS/Ironman7.wav", "http://novators.kz/audio/SuperheroesRUS/IronmanRUS/Ironman8.wav", "http://novators.kz/audio/SuperheroesRUS/IronmanRUS/Ironman9.wav", "http://novators.kz/audio/SuperheroesRUS/IronmanRUS/Ironman10.wav", "http://novators.kz/audio/SuperheroesRUS/IronmanRUS/Ironman11.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
