import sys
import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="James")
    furhat.say(url='http://novators.kz/audio/PolicemanRUS/PolicemanGameRUS/Policeman16.wav', lipsync=True)
    furhat.pauseSpeaking(10)
    url_list = [
        'http://novators.kz/audio/PolicemanRUS/PolicemanGameRUS/Policeman17.wav',
        'http://novators.kz/audio/PolicemanRUS/PolicemanGameRUS/Policeman18.wav',
        'http://novators.kz/audio/PolicemanRUS/PolicemanGameRUS/Policeman19.wav',
        'http://novators.kz/audio/PolicemanRUS/PolicemanGameRUS/Policeman20.wav',
        'http://novators.kz/audio/PolicemanRUS/PolicemanGameRUS/Policeman21.wav',
        'http://novators.kz/audio/PolicemanRUS/PolicemanGameRUS/Policeman22.wav',
        'http://novators.kz/audio/PolicemanRUS/PolicemanGameRUS/Policeman23.wav',
        'http://novators.kz/audio/PolicemanRUS/PolicemanGameRUS/Policeman24.wav',
    ]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
        time.sleep(10)
