
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/DictantRUS/ZayacRUS/ZayacRUS1.wav", "http://novators.kz/audio/DictantRUS/ZayacRUS/ZayacRUS2.wav", "http://novators.kz/audio/DictantRUS/ZayacRUS/ZayacRUS3.wav", "http://novators.kz/audio/DictantRUS/ZayacRUS/ZayacRUS4.wav", "http://novators.kz/audio/DictantRUS/ZayacRUS/ZayacRUS5.wav", "http://novators.kz/audio/DictantRUS/ZayacRUS/ZayacRUS6.wav", "http://novators.kz/audio/DictantRUS/ZayacRUS/ZayacRUS7.wav", "http://novators.kz/audio/DictantRUS/ZayacRUS/ZayacRUS8.wav", "http://novators.kz/audio/DictantRUS/ZayacRUS/ZayacRUS9.wav", "http://novators.kz/audio/DictantRUS/ZayacRUS/ZayacRUS10.wav", "http://novators.kz/audio/DictantRUS/ZayacRUS/ZayacRUS11.wav", "http://novators.kz/audio/DictantRUS/ZayacRUS/ZayacRUS12.wav", "http://novators.kz/audio/DictantRUS/ZayacRUS/ZayacRUS13.wav", "http://novators.kz/audio/DictantRUS/ZayacRUS/ZayacRUS14.wav", "http://novators.kz/audio/DictantRUS/ZayacRUS/ZayacRUS15.wav", "http://novators.kz/audio/DictantRUS/ZayacRUS/ZayacRUS16.wav", "http://novators.kz/audio/DictantRUS/ZayacRUS/ZayacRUS17.wav", "http://novators.kz/audio/DictantRUS/ZayacRUS/ZayacRUS18.wav", "http://novators.kz/audio/DictantRUS/ZayacRUS/ZayacRUS19.wav", "http://novators.kz/audio/DictantRUS/ZayacRUS/ZayacRUS20.wav", "http://novators.kz/audio/DictantRUS/ZayacRUS/ZayacRUS21.wav", "http://novators.kz/audio/DictantRUS/ZayacRUS/ZayacRUS22.wav", "http://novators.kz/audio/DictantRUS/ZayacRUS/ZayacRUS23.wav", "http://novators.kz/audio/DictantRUS/ZayacRUS/ZayacRUS24.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
