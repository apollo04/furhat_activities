
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/AdditionKAZ/AdditionKAZ1.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/AdditionKAZ/AdditionKAZ2.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/AdditionKAZ/AdditionKAZ3.wav", lipsync=True)
    time.sleep(35)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/AdditionKAZ/AdditionKAZ4.wav", lipsync=True)
    time.sleep(35)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/AdditionKAZ/AdditionKAZ5.wav", lipsync=True)
    time.sleep(30)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/AdditionKAZ/AdditionKAZ6.wav", lipsync=True)
    time.sleep(35)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/AdditionKAZ/AdditionKAZ7.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/AdditionKAZ/AdditionKAZ8.wav", lipsync=True)
    time.sleep(35)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/AdditionKAZ/AdditionKAZ10.wav", lipsync=True)
  
   
        
