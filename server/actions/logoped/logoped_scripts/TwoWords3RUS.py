
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Isabel")
    
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS9.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS10.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS11.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS12.wav", lipsync=True)