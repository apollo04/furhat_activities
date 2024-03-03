import sys
import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="Rania")

    url_list = [
        'http://novators.kz/audio/Cook/Cook_Zhent_RUS/cook-zhent-1-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_Zhent_RUS/cook-zhent-2-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_Zhent_RUS/cook-zhent-3-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_Zhent_RUS/cook-zhent-4-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_Zhent_RUS/cook-zhent-5-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_Zhent_RUS/cook-zhent-6-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_Zhent_RUS/cook-zhent-7-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_Zhent_RUS/cook-zhent-8-RUS.wav',
    ]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
        time.sleep(5)
