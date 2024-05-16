
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Alex")
    
    url_list = ["file:///home/furnix/resources/SuperheroesRUS/IronmanRUS/Ironman1.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/IronmanRUS/Ironman2.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/IronmanRUS/Ironman3.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/IronmanRUS/Ironman4.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/IronmanRUS/Ironman5.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/IronmanRUS/Ironman6.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/IronmanRUS/Ironman7.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/IronmanRUS/Ironman8.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/IronmanRUS/Ironman9.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/IronmanRUS/Ironman10.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/IronmanRUS/Ironman11.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
