
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Isabel")
    
    url_list = ["file:///home/furnix/resources/LogopedRUS/IntroRUS/IntroRUS.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
