import sys
import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="James")

    url_list = [
        'http://novators.kz/audio/PolicemanKAZ/PolicemanIntroKAZ/Policeman1.wav',
        'http://novators.kz/audio/PolicemanKAZ/PolicemanIntroKAZ/Policeman2.wav',
    ]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
        time.sleep(5)
