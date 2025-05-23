
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Samuel")
    
    url_list = ["file:///home/furnix/resources/Animals/Animals2/AnimalsKAZ/GiraffeKAZ/giraffeKAZ1.wav", 
                "file:///home/furnix/resources/Animals/Animals2/AnimalsSounds/giraffe.wav",
                "file:///home/furnix/resources/Animals/Animals2/AnimalsSounds/giraffe.wav",
                "file:///home/furnix/resources/Animals/Animals2/AnimalsSounds/giraffe.wav",
                "file:///home/furnix/resources/Animals/Animals1/AnimalsKAZ/GiraffeKAZ/giraffeKAZ2.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
