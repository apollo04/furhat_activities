import sys
import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="Rania")

    url_list = [
        'http://novators.kz/audio/Cook/Cook_Besh_KAZ/cook-besh-1-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Besh_KAZ/cook-besh-2-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Besh_KAZ/cook-besh-3-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Besh_KAZ/cook-besh-4-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Besh_KAZ/cook-besh-5-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Besh_KAZ/cook-besh-6-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Besh_KAZ/cook-besh-7-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Besh_KAZ/cook-besh-8-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Besh_KAZ/cook-besh-9-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Besh_KAZ/cook-besh-10-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Besh_KAZ/cook-besh-11-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Besh_KAZ/cook-besh-12-KAZ.wav',
    ]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
        time.sleep(5)
