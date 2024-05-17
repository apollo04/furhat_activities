
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    furhat.say(url="file:///home/furnix/resources/Counting/CountingRUS/Intro.wav", lipsync=True)