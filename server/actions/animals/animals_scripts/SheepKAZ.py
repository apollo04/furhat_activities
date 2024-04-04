
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Samuel")
    
    url_list = ["http://novators.kz/audio/Animals/Animals2/AnimalsKAZ/SheepKAZ/sheepKAZ1.wav", "http://novators.kz/audio/Animals/Animals2/AnimalsSounds/sheep.wav", "http://novators.kz/audio/Animals/Animals1/AnimalsKAZ/SheepKAZ/sheepKAZ2.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
