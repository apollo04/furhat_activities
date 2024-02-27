import sys
import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="Chen")

    url_list = [
        'http://novators.kz/audio/PolicemanRUS/RoadRulesRUS/Policeman11.wav',
        'http://novators.kz/audio/PolicemanRUS/RoadRulesRUS/Policeman12.wav',
        'http://novators.kz/audio/PolicemanRUS/RoadRulesRUS/Policeman13.wav',
    ]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
        time.sleep(5)
