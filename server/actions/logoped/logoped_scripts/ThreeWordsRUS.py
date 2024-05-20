
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Isabel")
    

    furhat.say(url="file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS1.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS2.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS3.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS4.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS5.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS6.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS7.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS8.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS9.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS10.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS11.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS12.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS13.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS14.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS15.wav", lipsync=True)

