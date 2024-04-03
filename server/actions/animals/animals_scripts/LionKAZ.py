
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yi")
    
    url_list = ["http://novators.kz/audio/Animals/Animals2/AnimalsKAZ/LionKAZ/lionKAZ1.wav", "http://novators.kz/audio/Animals/Animals2/AnimalsSounds/LionAudio.wav", "http://novators.kz/audio/Animals/Animals1/AnimalsKAZ/LionKAZ/lionKAZ2.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
