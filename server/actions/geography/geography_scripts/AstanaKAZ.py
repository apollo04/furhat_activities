
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/KazakhstanMapKAZ/AstanaKAZ/Astana1.wav", "http://novators.kz/audio/KazakhstanMapKAZ/AstanaKAZ/Astana2.wav", "http://novators.kz/audio/KazakhstanMapKAZ/AstanaKAZ/Astana3.wav", "http://novators.kz/audio/KazakhstanMapKAZ/AstanaKAZ/Astana4.wav", "http://novators.kz/audio/KazakhstanMapKAZ/AstanaKAZ/Astana5.wav", "http://novators.kz/audio/KazakhstanMapKAZ/AstanaKAZ/Astana6.wav", "http://novators.kz/audio/KazakhstanMapKAZ/AstanaKAZ/Astana7.wav", "http://novators.kz/audio/KazakhstanMapKAZ/AstanaKAZ/Astana8.wav", "http://novators.kz/audio/KazakhstanMapKAZ/AstanaKAZ/Astana9.wav", "http://novators.kz/audio/KazakhstanMapKAZ/AstanaKAZ/Astana10.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
