
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Alex")
    
    url_list = ["http://novators.kz/audio/SuperheroesRUS/SpidermanRUS/Spiderman1.wav", "http://novators.kz/audio/SuperheroesRUS/SpidermanRUS/Spiderman2.wav", "http://novators.kz/audio/SuperheroesRUS/SpidermanRUS/Spiderman3.wav", "http://novators.kz/audio/SuperheroesRUS/SpidermanRUS/Spiderman4.wav", "http://novators.kz/audio/SuperheroesRUS/SpidermanRUS/Spiderman5.wav", "http://novators.kz/audio/SuperheroesRUS/SpidermanRUS/Spiderman6.wav", "http://novators.kz/audio/SuperheroesRUS/SpidermanRUS/Spiderman7.wav", "http://novators.kz/audio/SuperheroesRUS/SpidermanRUS/Spiderman8.wav", "http://novators.kz/audio/SuperheroesRUS/SpidermanRUS/Spiderman9.wav", "http://novators.kz/audio/SuperheroesRUS/SpidermanRUS/Spiderman10.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
