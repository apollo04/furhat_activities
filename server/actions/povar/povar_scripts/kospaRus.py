import sys
import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="Rania")

    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Kospa_RUS/cook-kospa-1-RUS.wav', lipsync=True)
    time.sleep(30)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Kospa_RUS/cook-kospa-2-RUS.wav', lipsync=True)
    time.sleep(30)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Kospa_RUS/cook-kospa-3-RUS.wav', lipsync=True)
    time.sleep(30)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Kospa_RUS/cook-kospa-4-RUS.wav', lipsync=True)
    time.sleep(35)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Kospa_RUS/cook-kospa-5-RUS.wav', lipsync=True)
    time.sleep(10)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Kospa_RUS/cook-kospa-6-RUS.wav', lipsync=True)
    time.sleep(20)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Kospa_RUS/cook-kospa-7-RUS.wav', lipsync=True)

