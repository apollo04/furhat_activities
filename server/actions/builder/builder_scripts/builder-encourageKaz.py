import sys
import time
import random

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="James")

    # Generate a random number between 1 and 100 (inclusive)
    random_number = random.randint(1, 2)

    url_list = [
    'http://novators.kz/audio//BuilderKAZ/BuilderPraiseIncorrectKAZ/profPraiseWhenIncorrectKAZ' + str(random_number) + '.wav'
    ]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
        time.sleep(5)

