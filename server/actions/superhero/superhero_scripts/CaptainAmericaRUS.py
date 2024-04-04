
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Alex")
    
    url_list = ["http://novators.kz/audio/SuperheroesRUS/CaptainAmericaRUS/CaptainAmericaRUS1.wav",
                "http://novators.kz/audio/SuperheroesRUS/CaptainAmericaRUS/CaptainAmericaRUS2.wav", 
                "http://novators.kz/audio/SuperheroesRUS/CaptainAmericaRUS/CaptainAmericaRUS3.wav", 
                "http://novators.kz/audio/SuperheroesRUS/CaptainAmericaRUS/CaptainAmericaRUS4.wav", 
                "http://novators.kz/audio/SuperheroesRUS/CaptainAmericaRUS/CaptainAmericaRUS5.wav", 
                "http://novators.kz/audio/SuperheroesRUS/CaptainAmericaRUS/CaptainAmericaRUS6.wav", 
                "http://novators.kz/audio/SuperheroesRUS/CaptainAmericaRUS/CaptainAmericaRUS7.wav", 
                "http://novators.kz/audio/SuperheroesRUS/CaptainAmericaRUS/CaptainAmericaRUS8.wav", 
                "http://novators.kz/audio/SuperheroesRUS/CaptainAmericaRUS/CaptainAmericaRUS9.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)