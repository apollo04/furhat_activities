import sys
import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="Rania")

    furhat.say(url='file:///home/furnix/resources/Cook/Cook_NauryzKozhe_KAZ/cook-nauryz-kozhe-1-KAZ.wav', lipsync=True)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_NauryzKozhe_KAZ/cook-nauryz-kozhe-2-KAZ.wav', lipsync=True)
    time.sleep(35)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_NauryzKozhe_KAZ/cook-nauryz-kozhe-3-KAZ.wav', lipsync=True)
    time.sleep(25)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_NauryzKozhe_KAZ/cook-nauryz-kozhe-4-KAZ.wav', lipsync=True)
    time.sleep(35)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_NauryzKozhe_KAZ/cook-nauryz-kozhe-5-KAZ.wav', lipsync=True)
    time.sleep(30)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_NauryzKozhe_KAZ/cook-nauryz-kozhe-6-KAZ.wav', lipsync=True)
    time.sleep(30)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_NauryzKozhe_KAZ/cook-nauryz-kozhe-7-KAZ.wav', lipsync=True)
    time.sleep(30)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_NauryzKozhe_KAZ/cook-nauryz-kozhe-8-KAZ.wav', lipsync=True)
    time.sleep(25)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_NauryzKozhe_KAZ/cook-nauryz-kozhe-9-KAZ.wav', lipsync=True)
    

