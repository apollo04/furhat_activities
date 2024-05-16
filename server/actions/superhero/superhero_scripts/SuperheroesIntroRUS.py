
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Alex")
    
    url_list = ["file:///home/furnix/resources/SuperheroesRUS/IntroRUS/IntroRUS1.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/IntroRUS/IntroRUS2.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/IntroRUS/IntroRUS3.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/IntroRUS/IntroRUS4.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
