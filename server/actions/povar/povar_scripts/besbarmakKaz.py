import sys
import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="Rania")

    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Besh_KAZ/cook-besh-1-KAZ.wav', lipsync=True)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Besh_KAZ/cook-besh-2-KAZ.wav', lipsync=True)
    time.sleep(10)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Besh_KAZ/cook-besh-3-KAZ.wav', lipsync=True)
    time.sleep(25)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Besh_KAZ/cook-besh-4-KAZ.wav', lipsync=True)
    time.sleep(25)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Besh_KAZ/cook-besh-5-KAZ.wav', lipsync=True)
    time.sleep(25)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Besh_KAZ/cook-besh-6-KAZ.wav', lipsync=True)
    time.sleep(35)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Besh_KAZ/cook-besh-7-KAZ.wav', lipsync=True)
    time.sleep(30)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Besh_KAZ/cook-besh-8-KAZ.wav', lipsync=True)
    time.sleep(30)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Besh_KAZ/cook-besh-9-KAZ.wav', lipsync=True)
    time.sleep(30)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Besh_KAZ/cook-besh-10-KAZ.wav', lipsync=True)
    time.sleep(20)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Besh_KAZ/cook-besh-11-KAZ.wav', lipsync=True)
    time.sleep(5)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Besh_KAZ/cook-besh-12-KAZ.wav', lipsync=True)


    
