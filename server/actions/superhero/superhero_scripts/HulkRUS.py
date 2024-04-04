
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Alex")
    
    url_list = ["http://novators.kz/audio/SuperheroesRUS/HulkRUS/HulkRUS1.wav",
                "http://novators.kz/audio/SuperheroesRUS/HulkRUS/HulkRUS2.wav", 
                "http://novators.kz/audio/SuperheroesRUS/HulkRUS/HulkRUS3.wav", 
                "http://novators.kz/audio/SuperheroesRUS/HulkRUS/HulkRUS4.wav", 
                "http://novators.kz/audio/SuperheroesRUS/HulkRUS/HulkRUS5.wav", 
                "http://novators.kz/audio/SuperheroesRUS/HulkRUS/HulkRUS6.wav", 
                "http://novators.kz/audio/SuperheroesRUS/HulkRUS/HulkRUS7.wav", 
                "http://novators.kz/audio/SuperheroesRUS/HulkRUS/HulkRUS8.wav", 
                "http://novators.kz/audio/SuperheroesRUS/HulkRUS/HulkRUS9.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)