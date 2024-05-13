
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapRUS/AstanaRUS/Astana1.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AstanaRUS/Astana2.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AstanaRUS/Astana3.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AstanaRUS/Astana4.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AstanaRUS/Astana5.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AstanaRUS/Astana6.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AstanaRUS/Astana7.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AstanaRUS/Astana8.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AstanaRUS/Astana9.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
