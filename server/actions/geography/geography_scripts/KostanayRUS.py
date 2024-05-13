
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapRUS/KostanayRUS/Kostanay1.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/KostanayRUS/Kostanay2.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/KostanayRUS/Kostanay3.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/KostanayRUS/Kostanay4.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/KostanayRUS/Kostanay5.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/KostanayRUS/Kostanay6.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/KostanayRUS/Kostanay7.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/KostanayRUS/Kostanay8.wav", 
                "file:///home/furnix/resources/KazakhstanMapRUS/KostanayRUS/Kostanay9.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
