import sys
import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="Chen")

    url_list = [
        'http://novators.kz/audio/PolicemanKAZ/PolicemanGameKAZ/Policeman16.wav',
        'http://novators.kz/audio/PolicemanKAZ/PolicemanGameKAZ/Policeman17.wav',
        'http://novators.kz/audio/PolicemanKAZ/PolicemanGameKAZ/Policeman18.wav',
        'http://novators.kz/audio/PolicemanKAZ/PolicemanGameKAZ/Policeman19.wav',
        'http://novators.kz/audio/PolicemanKAZ/PolicemanGameKAZ/Policeman20.wav',
        'http://novators.kz/audio/PolicemanKAZ/PolicemanGameKAZ/Policeman21.wav',
        'http://novators.kz/audio/PolicemanKAZ/PolicemanGameKAZ/Policeman22.wav',
        'http://novators.kz/audio/PolicemanKAZ/PolicemanGameKAZ/Policeman23.wav',
        'http://novators.kz/audio/PolicemanKAZ/PolicemanGameKAZ/Policeman24.wav',
    ]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
        time.sleep(10)
