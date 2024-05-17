
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Alex")
    
    furhat.say(url="file:///home/furnix/resources/SuperheroesKAZ/IntroKAZ/IntroKAZ1.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/SuperheroesKAZ/IntroKAZ/IntroKAZ2.wav", lipsync=True)
    time.sleep(15)
    furhat.say(url="file:///home/furnix/resources/SuperheroesKAZ/IntroKAZ/IntroKAZ3.wav", lipsync=True)
    
