
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/AdditionRUS/AdditionRUS1.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/AdditionRUS/AdditionRUS2.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/AdditionRUS/AdditionRUS3.wav", lipsync=True)
    time.sleep(30)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/AdditionRUS/AdditionRUS4.wav", lipsync=True)
    time.sleep(30)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/AdditionRUS/AdditionRUS5.wav", lipsync=True)
    time.sleep(30)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/AdditionRUS/AdditionRUS6.wav", lipsync=True)
    time.sleep(30)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/AdditionRUS/AdditionRUS7.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/AdditionRUS/AdditionRUS8.wav", lipsync=True)
    time.sleep(30)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/AdditionRUS/AdditionRUS10.wav", lipsync=True)


 
