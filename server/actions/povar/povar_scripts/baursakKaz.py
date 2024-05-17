import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="Rania")

    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Baursak_KAZ/cook-baursak-1-KAZ.wav', lipsync=True)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Baursak_KAZ/cook-baursak-2-KAZ.wav', lipsync=True)
    time.sleep(12)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Baursak_KAZ/cook-baursak-3-KAZ.wav', lipsync=True)
    time.sleep(20)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Baursak_KAZ/cook-baursak-4-KAZ.wav', lipsync=True)
    time.sleep(35)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Baursak_KAZ/cook-baursak-5-KAZ.wav', lipsync=True)
    time.sleep(35)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Baursak_KAZ/cook-baursak-6-KAZ.wav', lipsync=True)
    time.sleep(30)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Baursak_KAZ/cook-baursak-7-KAZ.wav', lipsync=True)
    time.sleep(25)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Baursak_KAZ/cook-baursak-8-KAZ.wav', lipsync=True)
    time.sleep(25)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Baursak_KAZ/cook-baursak-9-KAZ.wav', lipsync=True)
    time.sleep(25)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Baursak_KAZ/cook-baursak-10-KAZ.wav', lipsync=True)
    time.sleep(30)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Baursak_KAZ/cook-baursak-11-KAZ.wav', lipsync=True)

