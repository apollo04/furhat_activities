import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="Rania")

    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Baursak_RUS/cook-baursak-1-RUS.wav', lipsync=True)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Baursak_RUS/cook-baursak-2-RUS.wav', lipsync=True)
    time.sleep(12)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Baursak_RUS/cook-baursak-3-RUS.wav', lipsync=True)
    time.sleep(20)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Baursak_RUS/cook-baursak-4-RUS.wav', lipsync=True)
    time.sleep(35)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Baursak_RUS/cook-baursak-5-RUS.wav', lipsync=True)
    time.sleep(30)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Baursak_RUS/cook-baursak-6-RUS.wav', lipsync=True)
    time.sleep(30)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Baursak_RUS/cook-baursak-7-RUS.wav', lipsync=True)
    time.sleep(30)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Baursak_RUS/cook-baursak-8-RUS.wav', lipsync=True)
    time.sleep(30)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Baursak_RUS/cook-baursak-9-RUS.wav', lipsync=True)
    time.sleep(30)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Baursak_RUS/cook-baursak-10-RUS.wav', lipsync=True)
    time.sleep(30)
    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Baursak_RUS/cook-baursak-11-RUS.wav', lipsync=True)


  
