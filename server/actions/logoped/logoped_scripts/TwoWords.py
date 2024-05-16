
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Isabel")
    
    url_list = ["file:///home/furnix/resources/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ1.wav", 
                "file:///home/furnix/resources/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ2.wav", 
                "file:///home/furnix/resources/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ3.wav", 
                "file:///home/furnix/resources/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ4.wav", 
                "file:///home/furnix/resources/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ5.wav", 
                "file:///home/furnix/resources/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ6.wav", 
                "file:///home/furnix/resources/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ7.wav", 
                "file:///home/furnix/resources/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ8.wav", 
                "file:///home/furnix/resources/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ9.wav", 
                "file:///home/furnix/resources/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ10.wav", 
                "file:///home/furnix/resources/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ11.wav", 
                "file:///home/furnix/resources/LogopedKAZ/TwoWordsKAZ/TwoWordsKAZ12.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
