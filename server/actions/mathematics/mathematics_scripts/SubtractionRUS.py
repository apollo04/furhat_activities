
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/SubtractionRUS/SubtractionRUS1.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/SubtractionRUS/SubtractionRUS2.wav", lipsync=True)
    time.sleep(15)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/SubtractionRUS/SubtractionRUS3.wav", lipsync=True)
    time.sleep(40)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/SubtractionRUS/SubtractionRUS4.wav", lipsync=True)
    time.sleep(40)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/SubtractionRUS/SubtractionRUS5.wav", lipsync=True)
    time.sleep(5)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/CountingNumbersRUS/oneRUS.wav", lipsync=True)
    time.sleep(5)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/CountingNumbersRUS/twoRUS.wav", lipsync=True)
    time.sleep(5)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/CountingNumbersRUS/threeRUS.wav", lipsync=True)
    time.sleep(30)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/SubtractionRUS/SubtractionRUS6.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/SubtractionRUS/SubtractionRUS7.wav", lipsync=True)
    time.sleep(40)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/SubtractionRUS/SubtractionRUS8.wav", lipsync=True)

