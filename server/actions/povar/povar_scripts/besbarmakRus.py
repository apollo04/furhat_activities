import sys
import time

from furhat_remote_api import FurhatRemoteAPI

furhat = FurhatRemoteAPI(sys.argv[1])

furhat.set_face(mask="adult", character="Rania")

url_list = [
    'http://novators.kz/audio/Cook/Cook_Besh_RUS/cook-besh-1-RUS.wav',
    'http://novators.kz/audio/Cook/Cook_Besh_RUS/cook-besh-2-RUS.wav',
    'http://novators.kz/audio/Cook/Cook_Besh_RUS/cook-besh-3-RUS.wav',
    'http://novators.kz/audio/Cook/Cook_Besh_RUS/cook-besh-4-RUS.wav',
    'http://novators.kz/audio/Cook/Cook_Besh_RUS/cook-besh-5-RUS.wav',
    'http://novators.kz/audio/Cook/Cook_Besh_RUS/cook-besh-6-RUS.wav',
    'http://novators.kz/audio/Cook/Cook_Besh_RUS/cook-besh-7-RUS.wav',
    'http://novators.kz/audio/Cook/Cook_Besh_RUS/cook-besh-8-RUS.wav',
    'http://novators.kz/audio/Cook/Cook_Besh_RUS/cook-besh-9-RUS.wav',
    'http://novators.kz/audio/Cook/Cook_Besh_RUS/cook-besh-10-RUS.wav',
    'http://novators.kz/audio/Cook/Cook_Besh_RUS/cook-besh-11-RUS.wav',
    'http://novators.kz/audio/Cook/Cook_Besh_RUS/cook-besh-12-RUS.wav',
]

for url in url_list:
    furhat.say(url=url, lipsync=True)
    time.sleep(5)
