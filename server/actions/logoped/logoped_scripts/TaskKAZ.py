
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Isabel")
    
    url_list = ["http://novators.kz/audio/LogopedKAZ/TaskKAZ/TaskKAZ1.wav", "http://novators.kz/audio/LogopedKAZ/TaskKAZ/TaskKAZ2.wav", "http://novators.kz/audio/LogopedKAZ/TaskKAZ/TaskKAZ3.wav", "http://novators.kz/audio/LogopedKAZ/TaskKAZ/TaskKAZ4.wav", "http://novators.kz/audio/LogopedKAZ/TaskKAZ/TaskKAZ5.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
