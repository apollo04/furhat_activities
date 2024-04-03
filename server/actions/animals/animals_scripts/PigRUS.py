
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Patricia")
    
    url_list = ["http://novators.kz/audio/Animals/Animals2/AnimalsRUS/PigRUS/pigRUS1.wav", "http://novators.kz/audio/Animals/Animals2/AnimalsSounds/PigAudio.wav", "http://novators.kz/audio/Animals/Animals1/AnimalsRUS/PigRUS/pigRUS2.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
