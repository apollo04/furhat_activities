import sys
import time
import random

from furhat_remote_api import FurhatRemoteAPI

furhat = FurhatRemoteAPI(sys.argv[1])

furhat.set_face(mask="adult", character="Rania")

numbers = [1, 2, 4]

# Choose a random number from the list
random_number = random.choice(numbers)


url_list = [
'http://novators.kz/audio/Cook/Cook_Questions_RUS/cook-praise-' + str(random_number) + '-RUS.wav'
]

for url in url_list:

    furhat.say(url=url, lipsync=True)
    time.sleep(5)




