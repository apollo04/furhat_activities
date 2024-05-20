
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Alex")
    
    url_list = ["file:///home/furnix/resources/SuperheroesRUS/SpidermanRUS/Spiderman1.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/SpidermanRUS/Spiderman2.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/SpidermanRUS/Spiderman3.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/SpidermanRUS/Spiderman4.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/SpidermanRUS/Spiderman5.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/SpidermanRUS/Spiderman6.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/SpidermanRUS/Spiderman7.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/SpidermanRUS/Spiderman8.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/SpidermanRUS/Spiderman10.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
