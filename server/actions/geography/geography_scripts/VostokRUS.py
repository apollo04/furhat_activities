
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapRUS/VostokRUS/Vostok1.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/VostokRUS/Vostok2.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/VostokRUS/Vostok3.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/VostokRUS/Vostok4.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/VostokRUS/Vostok5.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/VostokRUS/Vostok6.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/VostokRUS/Vostok7.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/VostokRUS/Vostok8.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/VostokRUS/Vostok9.wav",
                "file:///home/furnix/resources/KazakhstanMapRUS/VostokRUS/Vostok10.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)