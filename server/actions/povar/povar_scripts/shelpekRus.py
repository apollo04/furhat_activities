import sys
import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="Rania")

    url_list = [
        'http://novators.kz/audio/Cook/Cook_Shelpek_RUS/cook-shelpek-1-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_Shelpek_RUS/cook-shelpek-2-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_Shelpek_RUS/cook-shelpek-3-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_Shelpek_RUS/cook-shelpek-4-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_Shelpek_RUS/cook-shelpek-5-RUS.wav',
    ]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
        time.sleep(5)
