
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Alex")
    
    url_list = ["file:///home/furnix/resources/SuperheroesRUS/HulkRUS/HulkRUS1.wav",
                "file:///home/furnix/resources/SuperheroesRUS/HulkRUS/HulkRUS4.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/HulkRUS/HulkRUS5.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/HulkRUS/HulkRUS6.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/HulkRUS/HulkRUS7.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/HulkRUS/HulkRUS9.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)