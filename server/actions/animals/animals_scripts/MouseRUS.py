
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Patricia")
    
    url_list = ["file:///home/furnix/resources/Animals/Animals2/AnimalsRUS/MouseRUS/MouseRUS1.wav", 
                "file:///home/furnix/resources/Animals/Animals2/AnimalsSounds/MouseAudio.wav", 
                "file:///home/furnix/resources/Animals/Animals1/AnimalsRUS/MouseRUS/MouseRUS2.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
