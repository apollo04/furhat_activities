
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Isabel")
    

    furhat.say(url="file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS6.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS7.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS8.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS9.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/LogopedRUS/ThreeWordsRUS/ThreeWordsRUS10.wav", lipsync=True)