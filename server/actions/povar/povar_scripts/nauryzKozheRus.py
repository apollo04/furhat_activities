import sys
import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="Rania")

    furhat.say(url='file:///home/furnix/resources/Cook/Cook_NauryzKozhe_RUS/cook-nauryz-kozhe-1-RUS.wav', lipsync=True)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_NauryzKozhe_RUS/cook-nauryz-kozhe-2-RUS.wav', lipsync=True)
    time.sleep(30)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_NauryzKozhe_RUS/cook-nauryz-kozhe-3-RUS.wav', lipsync=True)
    time.sleep(25)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_NauryzKozhe_RUS/cook-nauryz-kozhe-4-RUS.wav', lipsync=True)
    time.sleep(30)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_NauryzKozhe_RUS/cook-nauryz-kozhe-5-RUS.wav', lipsync=True)
    time.sleep(30)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_NauryzKozhe_RUS/cook-nauryz-kozhe-6-RUS.wav', lipsync=True)
    time.sleep(30)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_NauryzKozhe_RUS/cook-nauryz-kozhe-7-RUS.wav', lipsync=True)
    time.sleep(30)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_NauryzKozhe_RUS/cook-nauryz-kozhe-8-RUS.wav', lipsync=True)
    time.sleep(25)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_NauryzKozhe_RUS/cook-nauryz-kozhe-9-RUS.wav', lipsync=True)


