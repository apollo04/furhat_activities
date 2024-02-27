import sys
import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="Rania")

    url_list = [
        'http://novators.kz/audio/Cook/Cook_Kospa_RUS/cook-kospa-1-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_Kospa_RUS/cook-kospa-2-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_Kospa_RUS/cook-kospa-3-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_Kospa_RUS/cook-kospa-4-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_Kospa_RUS/cook-kospa-5-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_Kospa_RUS/cook-kospa-6-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_Kospa_RUS/cook-kospa-7-RUS.wav',
    ]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
        time.sleep(5)
