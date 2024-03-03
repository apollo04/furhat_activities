
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/Counting/CountingKAZ/SubtractionKAZ/SubtractionKAZ1.wav", "http://novators.kz/audio/Counting/CountingKAZ/SubtractionKAZ/SubtractionKAZ2.wav", "http://novators.kz/audio/Counting/CountingKAZ/SubtractionKAZ/SubtractionKAZ3.wav", "http://novators.kz/audio/Counting/CountingKAZ/SubtractionKAZ/SubtractionKAZ4.wav", "http://novators.kz/audio/Counting/CountingKAZ/SubtractionKAZ/SubtractionKAZ5.wav", "http://novators.kz/audio/Counting/CountingKAZ/SubtractionKAZ/SubtractionKAZ6.wav", "http://novators.kz/audio/Counting/CountingKAZ/SubtractionKAZ/SubtractionKAZ7.wav", "http://novators.kz/audio/Counting/CountingKAZ/SubtractionKAZ/SubtractionKAZ8.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
