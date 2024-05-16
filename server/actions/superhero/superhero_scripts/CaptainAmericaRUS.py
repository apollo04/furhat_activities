
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Alex")
    
    url_list = ["file:///home/furnix/resources/SuperheroesRUS/CaptainAmericaRUS/CaptainAmericaRUS1.wav",
                "file:///home/furnix/resources/SuperheroesRUS/CaptainAmericaRUS/CaptainAmericaRUS2.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/CaptainAmericaRUS/CaptainAmericaRUS3.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/CaptainAmericaRUS/CaptainAmericaRUS4.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/CaptainAmericaRUS/CaptainAmericaRUS5.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/CaptainAmericaRUS/CaptainAmericaRUS6.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/CaptainAmericaRUS/CaptainAmericaRUS7.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/CaptainAmericaRUS/CaptainAmericaRUS8.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/CaptainAmericaRUS/CaptainAmericaRUS9.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)