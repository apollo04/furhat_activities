
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Isabel")
    
    url_list = ["file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS1.wav", 
                "file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS2.wav", 
                "file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS3.wav", 
                "file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS4.wav", 
                "file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS5.wav", 
                "file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS6.wav", 
                "file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS7.wav", 
                "file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS8.wav", 
                "file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS9.wav", 
                "file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS10.wav", 
                "file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS11.wav", 
                "file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS12.wav", 
                "file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS13.wav", 
                "file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS14.wav", 
                "file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS15.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
