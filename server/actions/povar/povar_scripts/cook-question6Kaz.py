import sys
import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="Rania")

    url_list = [
        'file:///home/furnix/resources/Cook/Cook_Questions_KAZ/cook-questions-7-KAZ.wav',
    ]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
        time.sleep(5)
