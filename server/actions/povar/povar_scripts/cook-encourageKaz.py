import sys
import time
import random

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="Rania")

    # Generate a random number between 1 and 100 (inclusive)
    random_number = random.randint(5, 6)

    url_list = [
    'http://novators.kz/audio/Cook/Cook_Questions_KAZ/cook-praise-' + str(random_number) + '-KAZ.wav'
    ]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
        time.sleep(5)




