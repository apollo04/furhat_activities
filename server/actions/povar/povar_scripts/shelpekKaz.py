import sys
import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="Rania")

    furhat.say(url='file:///home/furnix/resources/Cook/Cook_Shelpek_KAZ/cook-shelpek-1-KAZ.wav', lipsync=True)
    

    url_list = [
        'file:///home/furnix/resources/Cook/Cook_Shelpek_KAZ/cook-shelpek-1-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Shelpek_KAZ/cook-shelpek-2-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Shelpek_KAZ/cook-shelpek-3-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Shelpek_KAZ/cook-shelpek-4-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Shelpek_KAZ/cook-shelpek-5-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Shelpek_KAZ/cook-shelpek-6-KAZ.wav',
    ]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
        time.sleep(5)
