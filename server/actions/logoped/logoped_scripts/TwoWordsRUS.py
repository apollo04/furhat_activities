
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Isabel")
    
    url_list = ["file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS1.wav", 
                "file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS2.wav", 
                "file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS3.wav", 
                "file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS4.wav", 
                "file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS5.wav", 
                "file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS6.wav", 
                "file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS7.wav", 
                "file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS8.wav", 
                "file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS9.wav", 
                "file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS10.wav", 
                "file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS11.wav", 
                "file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS12.wav"]

    furhat.say(url="file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS1.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS2.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS3.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS4.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS5.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS6.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS7.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS8.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS9.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS10.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS11.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS12.wav", lipsync=True)
    
