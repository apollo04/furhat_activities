
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Alex")
    
    url_list = ["http://novators.kz/audio/SuperheroesKAZ/HulkKAZ/HulkKAZ1.wav",
                "http://novators.kz/audio/SuperheroesKAZ/HulkKAZ/HulkKAZ2.wav", 
                "http://novators.kz/audio/SuperheroesKAZ/HulkKAZ/HulkKAZ3.wav", 
                "http://novators.kz/audio/SuperheroesKAZ/HulkKAZ/HulkKAZ4.wav", 
                "http://novators.kz/audio/SuperheroesKAZ/HulkKAZ/HulkKAZ5.wav", 
                "http://novators.kz/audio/SuperheroesKAZ/HulkKAZ/HulkKAZ6.wav", 
                "http://novators.kz/audio/SuperheroesKAZ/HulkKAZ/HulkKAZ7.wav", 
                "http://novators.kz/audio/SuperheroesKAZ/HulkKAZ/HulkKAZ8.wav", 
                "http://novators.kz/audio/SuperheroesKAZ/HulkKAZ/HulkKAZ9.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)