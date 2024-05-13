
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapKAZ/AlmatyKAZ/Almaty1.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AlmatyKAZ/Almaty2.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AlmatyKAZ/Almaty3.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AlmatyKAZ/Almaty4.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AlmatyKAZ/Almaty5.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AlmatyKAZ/Almaty6.wav",
                "file:///home/furnix/resources/KazakhstanMapKAZ/AlmatyKAZ/Almaty7.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AlmatyKAZ/Almaty8.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AlmatyKAZ/Almaty9.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AlmatyKAZ/Almaty10.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AlmatyKAZ/Almaty11.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AlmatyKAZ/Almaty12.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AlmatyKAZ/Almaty13.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/AlmatyKAZ/Almaty14.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
