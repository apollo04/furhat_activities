
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Isabel")

    furhat.say(url="file:///home/furnix/resources/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ11.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ12.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ13.wav", lipsync=True)
    time.sleep(15)
    furhat.say(url="file:///home/furnix/resources/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ14.wav", lipsync=True)
    time.sleep(15)
    furhat.say(url="file:///home/furnix/resources/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ15.wav", lipsync=True)