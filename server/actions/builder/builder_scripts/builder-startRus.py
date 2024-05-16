import sys
import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="James")

    url_list = [
            'http://novators.kz/audio/BuilderRUS/BuilderIntroRUS/IntroRUS1.wav',
            'http://novators.kz/audio/BuilderRUS/BuilderIntroRUS/IntroRUS2.wav',
            'http://novators.kz/audio/BuilderRUS/BuilderIntroRUS/IntroRUS3.wav',
                    'http://novators.kz/audio/BuilderRUS/BuilderInfoRUS/InfoRUS1.wav',
        'http://novators.kz/audio/BuilderRUS/BuilderInfoRUS/InfoRUS2.wav',
        'http://novators.kz/audio/BuilderRUS/BuilderInfoRUS/InfoRUS3.wav'
    ]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
        time.sleep(5)
