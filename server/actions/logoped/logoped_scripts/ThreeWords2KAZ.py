
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Isabel")

    furhat.say(url="file:///home/furnix/resources/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ6.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ7.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ8.wav", lipsync=True)
    time.sleep(15)
    furhat.say(url="file:///home/furnix/resources/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ9.wav", lipsync=True)
    time.sleep(15)
    furhat.say(url="file:///home/furnix/resources/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ10.wav", lipsync=True)