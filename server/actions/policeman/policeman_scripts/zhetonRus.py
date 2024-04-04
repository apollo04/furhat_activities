import sys
import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="James")

    url_list = [
        'http://novators.kz/audio/PolicemanRUS/ZhetonRUS/Policeman3.wav',
        'http://novators.kz/audio/PolicemanRUS/ZhetonRUS/Policeman4.wav',
        'http://novators.kz/audio/PolicemanRUS/ZhetonRUS/Policeman5.wav',
    ]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
        time.sleep(5)
