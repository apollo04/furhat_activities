
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Isabel")
    
    furhat.say(url="file:///home/furnix/resources/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ1.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ2.wav", lipsync=True)
    time.sleep(25)
    furhat.say(url="file:///home/furnix/resources/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ3.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ4.wav", lipsync=True)
   