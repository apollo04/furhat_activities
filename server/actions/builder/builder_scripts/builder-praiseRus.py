import sys
import time
import random

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="James")

    numbers = random.randint(1, 4)

    # Choose a random number from the list
    random_number = random.choice(numbers)


    url_list = [
        'file:///home/furnix/resources/BuilderRUS/BuilderPraiseCorrectRUS/BuilderPraiseCorrectRUS' + str(random_number) + '.wav'
    ]

    for url in url_list:

        furhat.say(url=url, lipsync=True)
        time.sleep(5)




