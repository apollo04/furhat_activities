
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapKAZ/SoltustikKAZ/Soltustik1.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/SoltustikKAZ/Soltustik2.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/SoltustikKAZ/Soltustik3.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/SoltustikKAZ/Soltustik4.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/SoltustikKAZ/Soltustik5.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/SoltustikKAZ/Soltustik6.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/SoltustikKAZ/Soltustik7.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/SoltustikKAZ/Soltustik8.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/SoltustikKAZ/Soltustik9.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/SoltustikKAZ/Soltustik10.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
