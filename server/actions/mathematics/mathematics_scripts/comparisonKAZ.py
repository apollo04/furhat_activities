
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ1.wav", 
                "file:///home/furnix/resources/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ2.wav", 
                "file:///home/furnix/resources/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ3.wav", 
                "file:///home/furnix/resources/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ4.wav", 
                "file:///home/furnix/resources/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ5.wav", 
                "file:///home/furnix/resources/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ6.wav", 
                "file:///home/furnix/resources/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ7.wav", 
                "file:///home/furnix/resources/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ8.wav", 
                "file:///home/furnix/resources/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ9.wav", 
                "file:///home/furnix/resources/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ10.wav", 
                "file:///home/furnix/resources/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ11.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
        time.sleep(10)
