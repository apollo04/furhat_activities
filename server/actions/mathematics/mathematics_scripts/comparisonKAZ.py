
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ1.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ2.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ3.wav", lipsync=True)
    time.sleep(40)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ4.wav", lipsync=True)
    time.sleep(40)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ5.wav", lipsync=True)
    time.sleep(15)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ6.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ7.wav", lipsync=True)
    time.sleep(25)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ8.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ9.wav", lipsync=True)
    time.sleep(35)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/ComparisonKAZ/ComparisonKAZ11.wav", lipsync=True)

   

  
