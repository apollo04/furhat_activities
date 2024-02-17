import sys
import time

from furhat_remote_api import FurhatRemoteAPI

furhat = FurhatRemoteAPI(sys.argv[1])

furhat.set_face(mask="adult", character="Rania")

url_list = [
    'http://novators.kz/audio/Cook/Cook_Questions_RUS/cook-questions-4-RUS.wav',
]

for url in url_list:
    furhat.say(url=url, lipsync=True)
    time.sleep(5)
