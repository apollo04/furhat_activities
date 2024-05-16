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

    furhat.say(url='http://novators.kz/audio/PolicemanKAZ/ZhetonKAZ/Policeman3.wav', lipsync=True)
    time.sleep(5)
    furhat.say(url='http://novators.kz/audio/PolicemanKAZ/ZhetonKAZ/Policeman4.wav', lipsync=True)
    time.sleep(5)
    furhat.say(url='http://novators.kz/audio/PolicemanKAZ/ZhetonKAZ/Policeman5.wav', lipsync=True)
