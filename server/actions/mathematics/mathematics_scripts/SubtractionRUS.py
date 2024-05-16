
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/Counting/CountingRUS/SubtractionRUS/SubtractionRUS1.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/SubtractionRUS/SubtractionRUS2.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/SubtractionRUS/SubtractionRUS3.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/SubtractionRUS/SubtractionRUS4.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/SubtractionRUS/SubtractionRUS5.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/SubtractionRUS/SubtractionRUS6.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/SubtractionRUS/SubtractionRUS7.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/SubtractionRUS/SubtractionRUS8.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
