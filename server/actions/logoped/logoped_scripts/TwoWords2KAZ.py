
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Isabel")
  
    furhat.say(url="file:///home/furnix/resources/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ5.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ6.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ7.wav", lipsync=True)
    time.sleep(15)
    furhat.say(url="file:///home/furnix/resources/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ8.wav", lipsync=True)
    