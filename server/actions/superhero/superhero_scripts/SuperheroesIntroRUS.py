
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Alex")
    furhat.say(url="file:///home/furnix/resources/SuperheroesRUS/IntroRUS/IntroRUS1.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/SuperheroesRUS/IntroRUS/IntroRUS2.wav", lipsync=True)
    time.sleep(15)
    furhat.say(url="file:///home/furnix/resources/SuperheroesRUS/IntroRUS/IntroRUS3.wav", lipsync=True)
    url_list = ["file:///home/furnix/resources/SuperheroesRUS/IntroRUS/IntroRUS1.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/IntroRUS/IntroRUS2.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/IntroRUS/IntroRUS3.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/IntroRUS/IntroRUS4.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
