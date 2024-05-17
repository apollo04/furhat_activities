
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Samuel")
    
    url_list = ["file:///home/furnix/resources/Animals/Animals2/AnimalsKAZ/LionKAZ/lionKAZ1.wav", 
                "file:///home/furnix/resources/Animals/Animals2/AnimalsSounds/lion.wav", 
                "file:///home/furnix/resources/Animals/Animals1/AnimalsKAZ/LionKAZ/lionKAZ2.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
