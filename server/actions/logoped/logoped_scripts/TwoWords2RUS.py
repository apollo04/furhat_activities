
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Isabel")

    
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS5.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS6.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS7.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/TwoWordsRUS/TwoWordsRUS8.wav", lipsync=True)