import sys
import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="Rania")

    url_list = [
        'http://novators.kz/audio/Cook/Cook_Zhent_KAZ/cook-zhent-1-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Zhent_KAZ/cook-zhent-2-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Zhent_KAZ/cook-zhent-3-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Zhent_KAZ/cook-zhent-4-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Zhent_KAZ/cook-zhent-5-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Zhent_KAZ/cook-zhent-6-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Zhent_KAZ/cook-zhent-7-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Zhent_KAZ/cook-zhent-8-KAZ.wav',
    ]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
        time.sleep(5)
