
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/Counting/CountingKAZ/AdditionKAZ/AdditionKAZ1.wav", 
                "file:///home/furnix/resources/Counting/CountingKAZ/AdditionKAZ/AdditionKAZ2.wav", 
                "file:///home/furnix/resources/Counting/CountingKAZ/AdditionKAZ/AdditionKAZ3.wav", 
                "file:///home/furnix/resources/Counting/CountingKAZ/AdditionKAZ/AdditionKAZ4.wav", 
                "file:///home/furnix/resources/Counting/CountingKAZ/AdditionKAZ/AdditionKAZ5.wav", 
                "file:///home/furnix/resources/Counting/CountingKAZ/AdditionKAZ/AdditionKAZ6.wav", 
                "file:///home/furnix/resources/Counting/CountingKAZ/AdditionKAZ/AdditionKAZ7.wav", 
                "file:///home/furnix/resources/Counting/CountingKAZ/AdditionKAZ/AdditionKAZ10.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
        time.sleep(10)
