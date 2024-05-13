
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapRUS/AlmatyRUS/Almaty1.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AlmatyRUS/Almaty2.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AlmatyRUS/Almaty3.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AlmatyRUS/Almaty4.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AlmatyRUS/Almaty5.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AlmatyRUS/Almaty6.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AlmatyRUS/Almaty7.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AlmatyRUS/Almaty8.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AlmatyRUS/Almaty9.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AlmatyRUS/Almaty10.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AlmatyRUS/Almaty11.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AlmatyRUS/Almaty12.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/AlmatyRUS/Almaty13.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
