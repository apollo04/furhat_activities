
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Isabel")
    
    url_list = ["file:///home/furnix/resources/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ1.wav", 
                "file:///home/furnix/resources/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ2.wav", 
                "file:///home/furnix/resources/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ3.wav", 
                "file:///home/furnix/resources/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ4.wav", 
                "file:///home/furnix/resources/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ5.wav", 
                "file:///home/furnix/resources/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ6.wav", 
                "file:///home/furnix/resources/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ7.wav", 
                "file:///home/furnix/resources/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ8.wav", 
                "file:///home/furnix/resources/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ9.wav", 
                "file:///home/furnix/resources/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ10.wav", 
                "file:///home/furnix/resources/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ11.wav", 
                "file:///home/furnix/resources/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ12.wav", 
                "file:///home/furnix/resources/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ13.wav", 
                "file:///home/furnix/resources/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ14.wav", 
                "file:///home/furnix/resources/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ15.wav"]

    furhat.say(url="file:///home/furnix/resources/LogopedKAZ/ThreeWordsKAZ/ThreeWordsKAZ1.wav", lipsync=True)