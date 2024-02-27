
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Omar")
    
    url_list = ["http://novators.kz/audio/FirefighterKAZ/PraiseCorrectKAZ/profPraiseKAZ1.wav", "http://novators.kz/audio/FirefighterKAZ/PraiseCorrectKAZ/profPraiseKAZ2.wav", "http://novators.kz/audio/FirefighterKAZ/PraiseCorrectKAZ/profPraiseKAZ3.wav", "http://novators.kz/audio/FirefighterKAZ/PraiseCorrectKAZ/profPraiseKAZ4.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
