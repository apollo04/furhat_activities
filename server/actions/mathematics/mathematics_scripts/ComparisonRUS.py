
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/Counting/CountingRUS/ComparisonRUS/ComparisonRUS1.wav", "http://novators.kz/audio/Counting/CountingRUS/ComparisonRUS/ComparisonRUS2.wav", "http://novators.kz/audio/Counting/CountingRUS/ComparisonRUS/ComparisonRUS3.wav", "http://novators.kz/audio/Counting/CountingRUS/ComparisonRUS/ComparisonRUS4.wav", "http://novators.kz/audio/Counting/CountingRUS/ComparisonRUS/ComparisonRUS5.wav", "http://novators.kz/audio/Counting/CountingRUS/ComparisonRUS/ComparisonRUS6.wav", "http://novators.kz/audio/Counting/CountingRUS/ComparisonRUS/ComparisonRUS7.wav", "http://novators.kz/audio/Counting/CountingRUS/ComparisonRUS/ComparisonRUS8.wav", "http://novators.kz/audio/Counting/CountingRUS/ComparisonRUS/ComparisonRUS9.wav", "http://novators.kz/audio/Counting/CountingRUS/ComparisonRUS/ComparisonRUS10.wav", "http://novators.kz/audio/Counting/CountingRUS/ComparisonRUS/ComparisonRUS11.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
