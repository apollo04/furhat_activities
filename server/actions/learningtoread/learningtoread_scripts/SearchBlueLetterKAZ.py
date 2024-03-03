
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Zhen")
    
    url_list = ["http://novators.kz/audio/LearnToReadKAZ/SearchBlueLetterKAZ/SearchBlueLetterKAZ.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
