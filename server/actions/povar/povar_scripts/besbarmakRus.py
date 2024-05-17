import sys
import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="Rania")

    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Besh_RUS/cook-besh-1-RUS.wav', lipsync=True)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Besh_RUS/cook-besh-2-RUS.wav', lipsync=True)
    time.sleep(10)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Besh_RUS/cook-besh-3-RUS.wav', lipsync=True)
    time.sleep(25)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Besh_RUS/cook-besh-4-RUS.wav', lipsync=True)
    time.sleep(25)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Besh_RUS/cook-besh-5-RUS.wav', lipsync=True)
    time.sleep(25)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Besh_RUS/cook-besh-6-RUS.wav', lipsync=True)
    time.sleep(35)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Besh_RUS/cook-besh-7-RUS.wav', lipsync=True)
    time.sleep(30)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Besh_RUS/cook-besh-8-RUS.wav', lipsync=True)
    time.sleep(30)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Besh_RUS/cook-besh-9-RUS.wav', lipsync=True)
    time.sleep(30)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Besh_RUS/cook-besh-10-RUS.wav', lipsync=True)
    time.sleep(20)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Besh_RUS/cook-besh-11-RUS.wav', lipsync=True)
    time.sleep(5)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Besh_RUS/cook-besh-12-RUS.wav', lipsync=True)



