
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Samuel")
    
    url_list = ["file:///home/furnix/resources/Animals/Animals2/AnimalsKAZ/ZebraKAZ/zebraKAZ1.wav", 
                "file:///home/furnix/resources/Animals/Animals2/AnimalsSounds/zebra.wav", 
                "file:///home/furnix/resources/Animals/Animals1/AnimalsKAZ/ZebraKAZ/zebraKAZ2.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
