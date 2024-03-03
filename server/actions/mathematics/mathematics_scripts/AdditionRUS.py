
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/Counting/CountingRUS/AdditionRUS/AdditionRUS1.wav", "http://novators.kz/audio/Counting/CountingRUS/AdditionRUS/AdditionRUS2.wav", "http://novators.kz/audio/Counting/CountingRUS/AdditionRUS/AdditionRUS3.wav", "http://novators.kz/audio/Counting/CountingRUS/AdditionRUS/AdditionRUS4.wav", "http://novators.kz/audio/Counting/CountingRUS/AdditionRUS/AdditionRUS5.wav", "http://novators.kz/audio/Counting/CountingRUS/AdditionRUS/AdditionRUS6.wav", "http://novators.kz/audio/Counting/CountingRUS/AdditionRUS/AdditionRUS7.wav", "http://novators.kz/audio/Counting/CountingRUS/AdditionRUS/AdditionRUS8.wav", "http://novators.kz/audio/Counting/CountingRUS/AdditionRUS/AdditionRUS9.wav", "http://novators.kz/audio/Counting/CountingRUS/AdditionRUS/AdditionRUS10.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
