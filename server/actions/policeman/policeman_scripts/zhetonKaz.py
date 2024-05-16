import sys
import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="James")

    url_list = [
        'http://novators.kz/audio/PolicemanKAZ/ZhetonKAZ/Policeman3.wav',
        'http://novators.kz/audio/PolicemanKAZ/ZhetonKAZ/Policeman4.wav',
        'http://novators.kz/audio/PolicemanKAZ/ZhetonKAZ/Policeman5.wav',
    ]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
        time.sleep(10)
