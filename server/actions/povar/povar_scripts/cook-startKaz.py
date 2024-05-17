import sys
import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="Rania")

    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Intro_KAZ/cook-intro-1-KAZ.wav', lipsync=True)
    time.sleep(10)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Intro_KAZ/cook-intro-2-KAZ.wav', lipsync=True)
    time.sleep(5)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Intro_KAZ/cook-intro-3-KAZ.wav', lipsync=True)
    time.sleep(5)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Intro_KAZ/cook-intro-4-KAZ.wav', lipsync=True)
    time.sleep(5)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Intro_KAZ/cook-intro-5-KAZ.wav', lipsync=True)
    time.sleep(5)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Intro_KAZ/cook-intro-6-KAZ.wav', lipsync=True)

