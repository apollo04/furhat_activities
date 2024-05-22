
import time
from furhat_remote_api import FurhatRemoteAPI


def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/ComparisonRUS/ComparisonRUS1.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/ComparisonRUS/ComparisonRUS2.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/ComparisonRUS/ComparisonRUS3.wav", lipsync=True)
    time.sleep(30)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/ComparisonRUS/ComparisonRUS4.wav", lipsync=True)
    time.sleep(30)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/ComparisonRUS/ComparisonRUS5.wav", lipsync=True)
    time.sleep(12)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/ComparisonRUS/ComparisonRUS6.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/ComparisonRUS/ComparisonRUS7.wav", lipsync=True)
    time.sleep(10)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/ComparisonRUS/ComparisonRUS8.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/ComparisonRUS/ComparisonRUS9.wav", lipsync=True)
    time.sleep(35)
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/ComparisonRUS/ComparisonRUS11.wav", lipsync=True)
