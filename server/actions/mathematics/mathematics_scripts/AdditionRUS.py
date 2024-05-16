
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/Counting/CountingRUS/AdditionRUS/AdditionRUS1.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/AdditionRUS/AdditionRUS2.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/AdditionRUS/AdditionRUS3.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/AdditionRUS/AdditionRUS4.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/AdditionRUS/AdditionRUS5.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/AdditionRUS/AdditionRUS6.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/AdditionRUS/AdditionRUS7.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/AdditionRUS/AdditionRUS8.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/AdditionRUS/AdditionRUS9.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/AdditionRUS/AdditionRUS10.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
