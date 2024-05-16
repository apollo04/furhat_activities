
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Alex")
    
    url_list = ["file:///home/furnix/resources/SuperheroesKAZ/SpidermanKAZ/Spiderman1.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/SpidermanKAZ/Spiderman2.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/SpidermanKAZ/Spiderman3.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/SpidermanKAZ/Spiderman4.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/SpidermanKAZ/Spiderman5.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/SpidermanKAZ/Spiderman6.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/SpidermanKAZ/Spiderman7.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/SpidermanKAZ/Spiderman8.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/SpidermanKAZ/Spiderman9.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/SpidermanKAZ/Spiderman10.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
