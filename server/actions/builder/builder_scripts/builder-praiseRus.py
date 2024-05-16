import sys
import time
import random

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="James")

    random_number = random.randint(1, 4)

    # Choose a random number from the list
    random_number = random.choice(numbers)


    url_list = [
        'http://novators.kz/audio/BuilderRUS/BuilderPraiseCorrectRUS/BuilderPraiseCorrectRUS' + str(random_number) + '.wav'
    ]

    for url in url_list:

        furhat.say(url=url, lipsync=True)
        time.sleep(5)




