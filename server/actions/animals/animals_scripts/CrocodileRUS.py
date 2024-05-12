
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Patricia")
    
    url_list = ["file:///home/furnix/resources/Animals/Animals2/AnimalsRUS/CrocodileRUS/crocodileRUS1.wav", 
                "file:///home/furnix/resources/Animals/Animals2/AnimalsSounds/CrocodileAudio.wav", 
                "file:///home/furnix/resources/Animals/Animals2/AnimalsRUS/CrocodileRUS/crocodileRUS2.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
