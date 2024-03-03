
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/Counting/CountingRUS/SubtractionRUS/SubtractionRUS1.wav", "http://novators.kz/audio/Counting/CountingRUS/SubtractionRUS/SubtractionRUS2.wav", "http://novators.kz/audio/Counting/CountingRUS/SubtractionRUS/SubtractionRUS3.wav", "http://novators.kz/audio/Counting/CountingRUS/SubtractionRUS/SubtractionRUS4.wav", "http://novators.kz/audio/Counting/CountingRUS/SubtractionRUS/SubtractionRUS5.wav", "http://novators.kz/audio/Counting/CountingRUS/SubtractionRUS/SubtractionRUS6.wav", "http://novators.kz/audio/Counting/CountingRUS/SubtractionRUS/SubtractionRUS7.wav", "http://novators.kz/audio/Counting/CountingRUS/SubtractionRUS/SubtractionRUS8.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
