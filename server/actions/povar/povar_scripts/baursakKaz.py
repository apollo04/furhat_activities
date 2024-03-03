import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)

    furhat.set_face(mask="adult", character="Rania")

    url_list = [
        'http://novators.kz/audio/Cook/Cook_Baursak_KAZ/cook-baursak-1-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Baursak_KAZ/cook-baursak-2-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Baursak_KAZ/cook-baursak-3-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Baursak_KAZ/cook-baursak-4-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Baursak_KAZ/cook-baursak-5-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Baursak_KAZ/cook-baursak-6-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Baursak_KAZ/cook-baursak-7-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Baursak_KAZ/cook-baursak-8-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Baursak_KAZ/cook-baursak-9-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Baursak_KAZ/cook-baursak-10-KAZ.wav',
        'http://novators.kz/audio/Cook/Cook_Baursak_KAZ/cook-baursak-11-KAZ.wav',
    ]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
        time.sleep(5)
