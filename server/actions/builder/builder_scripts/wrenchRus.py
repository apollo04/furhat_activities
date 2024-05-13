import sys
import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="James")

    url_list = [
        'http://novators.kz/audio/BuilderRUS/GaechnyiKluchRUS/GaechnyiKluchRUS.wav',
        'file:///home/furnix/resources/BuilderRUS/builderInstrumentsEndingRUS'
    ]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
        time.sleep(5)
