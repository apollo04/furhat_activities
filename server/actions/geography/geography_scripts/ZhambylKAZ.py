
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/KazakhstanMapKAZ/ZhambylKAZ/Zhambyl1.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/ZhambylKAZ/Zhambyl2.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/ZhambylKAZ/Zhambyl3.wav", 
                "file:///home/furnix/resources/KazakhstanMapKAZ/ZhambylKAZ/Zhambyl4.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)

