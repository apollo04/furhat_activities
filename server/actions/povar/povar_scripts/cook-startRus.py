import sys
import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="Rania")

    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Intro_Rus/cook-intro-1-RUS.wav', lipsync=True)
    time.sleep(5)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Intro_Rus/cook-intro-2-RUS.wav', lipsync=True)
    time.sleep(5)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Intro_Rus/cook-intro-3-RUS.wav', lipsync=True)
    time.sleep(5)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Intro_Rus/cook-intro-4-RUS.wav', lipsync=True)
    time.sleep(5)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Intro_Rus/cook-intro-5-RUS.wav', lipsync=True)
    time.sleep(5)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Intro_Rus/cook-intro-6-RUS.wav', lipsync=True)

   