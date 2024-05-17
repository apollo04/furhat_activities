
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")

    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/SubtractionKAZ/SubtractionKAZ1.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/SubtractionKAZ/SubtractionKAZ2.wav", lipsync=True)
    time.sleep(15)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/SubtractionKAZ/SubtractionKAZ3.wav", lipsync=True)
    time.sleep(40)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/SubtractionKAZ/SubtractionKAZ4.wav", lipsync=True)
    time.sleep(40)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/SubtractionKAZ/SubtractionKAZ5.wav", lipsync=True)
    time.sleep(7)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/CountingNumbersKAZ/oneKAZ.wav", lipsync=True)
    time.sleep(5)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/CountingNumbersKAZ/twoKAZ.wav", lipsync=True)
    time.sleep(5)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/CountingNumbersKAZ/threeKAZ.wav", lipsync=True)
    time.sleep(30)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/SubtractionKAZ/SubtractionKAZ6.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/SubtractionKAZ/SubtractionKAZ7.wav", lipsync=True)
    time.sleep(40)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingKAZ/SubtractionKAZ/SubtractionKAZ8.wav", lipsync=True)

