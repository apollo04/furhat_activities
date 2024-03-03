
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/DictantKAZ/ElephantKAZ/Elephant1.wav", "http://novators.kz/audio/DictantKAZ/ElephantKAZ/Elephant2.wav", "http://novators.kz/audio/DictantKAZ/ElephantKAZ/Elephant3.wav", "http://novators.kz/audio/DictantKAZ/ElephantKAZ/Elephant4.wav", "http://novators.kz/audio/DictantKAZ/ElephantKAZ/Elephant5.wav", "http://novators.kz/audio/DictantKAZ/ElephantKAZ/Elephant6.wav", "http://novators.kz/audio/DictantKAZ/ElephantKAZ/Elephant7.wav", "http://novators.kz/audio/DictantKAZ/ElephantKAZ/Elephant8.wav", "http://novators.kz/audio/DictantKAZ/ElephantKAZ/Elephant9.wav", "http://novators.kz/audio/DictantKAZ/ElephantKAZ/Elephant10.wav", "http://novators.kz/audio/DictantKAZ/ElephantKAZ/Elephant11.wav", "http://novators.kz/audio/DictantKAZ/ElephantKAZ/Elephant12.wav", "http://novators.kz/audio/DictantKAZ/ElephantKAZ/Elephant13.wav", "http://novators.kz/audio/DictantKAZ/ElephantKAZ/Elephant14.wav", "http://novators.kz/audio/DictantKAZ/ElephantKAZ/Elephant15.wav", "http://novators.kz/audio/DictantKAZ/ElephantKAZ/Elephant16.wav", "http://novators.kz/audio/DictantKAZ/ElephantKAZ/Elephant17.wav", "http://novators.kz/audio/DictantKAZ/ElephantKAZ/Elephant18.wav", "http://novators.kz/audio/DictantKAZ/ElephantKAZ/Elephant19.wav", "http://novators.kz/audio/DictantKAZ/ElephantKAZ/Elephant20.wav", "http://novators.kz/audio/DictantKAZ/ElephantKAZ/Elephant21.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
