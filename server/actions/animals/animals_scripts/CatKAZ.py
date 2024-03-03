
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yi")
    
    url_list = ["http://novators.kz/audio/Animals/Animals2/AnimalsKAZ/CatKAZ/catKAZ1.wav", "http://novators.kz/audio/Animals/Animals2/AnimalsSounds/cat.wav", "http://novators.kz/audio/Animals/Animals2/AnimalsKAZ/CatKAZ/catKAZ2.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
