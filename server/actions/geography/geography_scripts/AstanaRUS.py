
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/KazakhstanMapRUS/AstanaRUS/Astana1.wav", "http://novators.kz/audio/KazakhstanMapRUS/AstanaRUS/Astana2.wav", "http://novators.kz/audio/KazakhstanMapRUS/AstanaRUS/Astana3.wav", "http://novators.kz/audio/KazakhstanMapRUS/AstanaRUS/Astana4.wav", "http://novators.kz/audio/KazakhstanMapRUS/AstanaRUS/Astana5.wav", "http://novators.kz/audio/KazakhstanMapRUS/AstanaRUS/Astana6.wav", "http://novators.kz/audio/KazakhstanMapRUS/AstanaRUS/Astana7.wav", "http://novators.kz/audio/KazakhstanMapRUS/AstanaRUS/Astana8.wav", "http://novators.kz/audio/KazakhstanMapRUS/AstanaRUS/Astana9.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
