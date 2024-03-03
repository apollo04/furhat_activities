
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/KazakhstanMapKAZ/SoltustikKAZ/Soltustik1.wav", "http://novators.kz/audio/KazakhstanMapKAZ/SoltustikKAZ/Soltustik2.wav", "http://novators.kz/audio/KazakhstanMapKAZ/SoltustikKAZ/Soltustik3.wav", "http://novators.kz/audio/KazakhstanMapKAZ/SoltustikKAZ/Soltustik4.wav", "http://novators.kz/audio/KazakhstanMapKAZ/SoltustikKAZ/Soltustik5.wav", "http://novators.kz/audio/KazakhstanMapKAZ/SoltustikKAZ/Soltustik6.wav", "http://novators.kz/audio/KazakhstanMapKAZ/SoltustikKAZ/Soltustik7.wav", "http://novators.kz/audio/KazakhstanMapKAZ/SoltustikKAZ/Soltustik8.wav", "http://novators.kz/audio/KazakhstanMapKAZ/SoltustikKAZ/Soltustik9.wav", "http://novators.kz/audio/KazakhstanMapKAZ/SoltustikKAZ/Soltustik10.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
