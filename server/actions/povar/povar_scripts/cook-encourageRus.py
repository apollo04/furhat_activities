import sys
import time
import random

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="Rania")

    numbers = [3, 5, 6, 7]

    # Choose a random number from the list
    random_number = random.choice(numbers)


    url_list = [
    'file:///home/furnix/resources/Cook/Cook_Questions_RUS/cook-praise-' + str(random_number) + '-RUS.wav'
    ]

    for url in url_list:

        furhat.say(url=url, lipsync=True)
        time.sleep(5)




