
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapKAZ/AstanaKAZ/Astana1.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AstanaKAZ/Astana2.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AstanaKAZ/Astana3.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AstanaKAZ/Astana4.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AstanaKAZ/Astana5.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AstanaKAZ/Astana6.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AstanaKAZ/Astana7.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AstanaKAZ/Astana8.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AstanaKAZ/Astana9.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AstanaKAZ/Astana10.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
