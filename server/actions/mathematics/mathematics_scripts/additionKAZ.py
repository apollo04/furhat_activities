
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/Counting/CountingKAZ/AdditionKAZ/AdditionKAZ1.wav", "http://novators.kz/audio/Counting/CountingKAZ/AdditionKAZ/AdditionKAZ2.wav", "http://novators.kz/audio/Counting/CountingKAZ/AdditionKAZ/AdditionKAZ3.wav", "http://novators.kz/audio/Counting/CountingKAZ/AdditionKAZ/AdditionKAZ4.wav", "http://novators.kz/audio/Counting/CountingKAZ/AdditionKAZ/AdditionKAZ5.wav", "http://novators.kz/audio/Counting/CountingKAZ/AdditionKAZ/AdditionKAZ6.wav", "http://novators.kz/audio/Counting/CountingKAZ/AdditionKAZ/AdditionKAZ7.wav", "http://novators.kz/audio/Counting/CountingKAZ/AdditionKAZ/AdditionKAZ8.wav", "http://novators.kz/audio/Counting/CountingKAZ/AdditionKAZ/AdditionKAZ9.wav", "http://novators.kz/audio/Counting/CountingKAZ/AdditionKAZ/AdditionKAZ10.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
