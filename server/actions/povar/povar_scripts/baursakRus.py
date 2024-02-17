import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="Rania")

    url_list = [
        'http://novators.kz/audio/Cook/Cook_Baursak_RUS/cook-baursak-1-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_Baursak_RUS/cook-baursak-2-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_Baursak_RUS/cook-baursak-3-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_Baursak_RUS/cook-baursak-4-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_Baursak_RUS/cook-baursak-5-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_Baursak_RUS/cook-baursak-6-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_Baursak_RUS/cook-baursak-7-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_Baursak_RUS/cook-baursak-8-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_Baursak_RUS/cook-baursak-9-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_Baursak_RUS/cook-baursak-10-RUS.wav',
        'http://novators.kz/audio/Cook/Cook_Baursak_RUS/cook-baursak-11-RUS.wav',
    ]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
