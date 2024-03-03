
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/KazakhstanMapRUS/SoltustikRUS/Soltustik1.wav", "http://novators.kz/audio/KazakhstanMapRUS/SoltustikRUS/Soltustik2.wav", "http://novators.kz/audio/KazakhstanMapRUS/SoltustikRUS/Soltustik3.wav", "http://novators.kz/audio/KazakhstanMapRUS/SoltustikRUS/Soltustik4.wav", "http://novators.kz/audio/KazakhstanMapRUS/SoltustikRUS/Soltustik5.wav", "http://novators.kz/audio/KazakhstanMapRUS/SoltustikRUS/Soltustik6.wav", "http://novators.kz/audio/KazakhstanMapRUS/SoltustikRUS/Soltustik7.wav", "http://novators.kz/audio/KazakhstanMapRUS/SoltustikRUS/Soltustik8.wav", "http://novators.kz/audio/KazakhstanMapRUS/SoltustikRUS/Soltustik9.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
