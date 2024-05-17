import sys
import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="Rania")

    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Kospa_KAZ/cook-kospa-1-KAZ.wav', lipsync=True)
    time.sleep(12)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Kospa_KAZ/cook-kospa-2-KAZ.wav', lipsync=True)
    time.sleep(30)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Kospa_KAZ/cook-kospa-3-KAZ.wav', lipsync=True)
    time.sleep(30)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Kospa_KAZ/cook-kospa-4-KAZ.wav', lipsync=True)
    time.sleep(35)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Kospa_KAZ/cook-kospa-5-KAZ.wav', lipsync=True)
    time.sleep(10)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Kospa_KAZ/cook-kospa-6-KAZ.wav', lipsync=True)
    time.sleep(20)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Kospa_KAZ/cook-kospa-7-KAZ.wav', lipsync=True)


    
