
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jamie")
    
    url_list = ["http://novators.kz/audio/PilotRUS/PraiseIncorrectRUS/PraiseIncorrectRUS1.wav", "http://novators.kz/audio/PilotRUS/PraiseIncorrectRUS/PraiseIncorrectRUS2.wav", "http://novators.kz/audio/PilotRUS/PraiseIncorrectRUS/PraiseIncorrectRUS3.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
