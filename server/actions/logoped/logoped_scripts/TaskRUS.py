
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Isabel")
    
    url_list = ["http://novators.kz/audio/LogopedRUS/TaskRUS/TaskRUS1.wav", "http://novators.kz/audio/LogopedRUS/TaskRUS/TaskRUS2.wav", "http://novators.kz/audio/LogopedRUS/TaskRUS/TaskRUS3.wav", "http://novators.kz/audio/LogopedRUS/TaskRUS/TaskRUS4.wav", "http://novators.kz/audio/LogopedRUS/TaskRUS/TaskRUS5.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
