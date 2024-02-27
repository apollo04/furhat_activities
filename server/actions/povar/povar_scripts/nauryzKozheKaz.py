import sys
import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="Rania")

    url_list = [
        'http://novators.kz/audio/Cook/Cook_NauryzKozhe_KAZ/cook-nauryz-kozhe-1-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_NauryzKozhe_KAZ/cook-nauryz-kozhe-2-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_NauryzKozhe_KAZ/cook-nauryz-kozhe-3-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_NauryzKozhe_KAZ/cook-nauryz-kozhe-4-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_NauryzKozhe_KAZ/cook-nauryz-kozhe-5-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_NauryzKozhe_KAZ/cook-nauryz-kozhe-6-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_NauryzKozhe_KAZ/cook-nauryz-kozhe-7-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_NauryzKozhe_KAZ/cook-nauryz-kozhe-8-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_NauryzKozhe_KAZ/cook-nauryz-kozhe-9-KAZ.wav',
    ]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
        time.sleep(5)
