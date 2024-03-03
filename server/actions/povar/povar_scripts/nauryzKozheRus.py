import sys
import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="Rania")

    url_list = [
        'http://novators.kz/audio/Cook/Cook_NauryzKozhe_RUS/cook-nauryz-kozhe-1-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_NauryzKozhe_RUS/cook-nauryz-kozhe-2-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_NauryzKozhe_RUS/cook-nauryz-kozhe-3-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_NauryzKozhe_RUS/cook-nauryz-kozhe-4-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_NauryzKozhe_RUS/cook-nauryz-kozhe-5-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_NauryzKozhe_RUS/cook-nauryz-kozhe-6-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_NauryzKozhe_RUS/cook-nauryz-kozhe-7-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_NauryzKozhe_RUS/cook-nauryz-kozhe-8-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_NauryzKozhe_RUS/cook-nauryz-kozhe-9-RUS.wav',
    ]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
        time.sleep(5)
