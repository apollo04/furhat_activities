
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ1.wav", "http://novators.kz/audio/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ2.wav", "http://novators.kz/audio/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ3.wav", "http://novators.kz/audio/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ4.wav", "http://novators.kz/audio/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ5.wav", "http://novators.kz/audio/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ6.wav", "http://novators.kz/audio/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ7.wav", "http://novators.kz/audio/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ8.wav", "http://novators.kz/audio/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ9.wav", "http://novators.kz/audio/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ10.wav", "http://novators.kz/audio/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ11.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
