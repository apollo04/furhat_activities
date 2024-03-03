
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Alex")
    
    url_list = ["http://novators.kz/audio/SuperheroesKAZ/SpidermanKAZ/Spiderman1.wav", "http://novators.kz/audio/SuperheroesKAZ/SpidermanKAZ/Spiderman2.wav", "http://novators.kz/audio/SuperheroesKAZ/SpidermanKAZ/Spiderman3.wav", "http://novators.kz/audio/SuperheroesKAZ/SpidermanKAZ/Spiderman4.wav", "http://novators.kz/audio/SuperheroesKAZ/SpidermanKAZ/Spiderman5.wav", "http://novators.kz/audio/SuperheroesKAZ/SpidermanKAZ/Spiderman6.wav", "http://novators.kz/audio/SuperheroesKAZ/SpidermanKAZ/Spiderman7.wav", "http://novators.kz/audio/SuperheroesKAZ/SpidermanKAZ/Spiderman8.wav", "http://novators.kz/audio/SuperheroesKAZ/SpidermanKAZ/Spiderman9.wav", "http://novators.kz/audio/SuperheroesKAZ/SpidermanKAZ/Spiderman10.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
