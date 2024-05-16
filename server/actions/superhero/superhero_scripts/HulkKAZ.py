
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Alex")
    
    url_list = ["file:///home/furnix/resources/SuperheroesKAZ/HulkKAZ/HulkKAZ1.wav",
                "file:///home/furnix/resources/SuperheroesKAZ/HulkKAZ/HulkKAZ2.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/HulkKAZ/HulkKAZ3.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/HulkKAZ/HulkKAZ4.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/HulkKAZ/HulkKAZ5.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/HulkKAZ/HulkKAZ6.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/HulkKAZ/HulkKAZ7.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/HulkKAZ/HulkKAZ8.wav", 
                "file:///home/furnix/resources/SuperheroesKAZ/HulkKAZ/HulkKAZ9.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)