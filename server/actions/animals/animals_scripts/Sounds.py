
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yi")
    
 
    url_list = ["file:///home/furnix/resources/Animals/Animals2/AnimalsSounds/cat.wav", 
                "file:///home/furnix/resources/Animals/Animals2/AnimalsSounds/cow.wav",
                "file:///home/furnix/resources/Animals/Animals2/AnimalsSounds/crocodile.wav", 
                "file:///home/furnix/resources/Animals/Animals2/AnimalsSounds/dog.wav", 
                "file:///home/furnix/resources/Animals/Animals2/AnimalsSounds/elephant.wav", 
                "file:///home/furnix/resources/Animals/Animals2/AnimalsSounds/frog.wav",
                "file:///home/furnix/resources/Animals/Animals2/AnimalsSounds/giraffe.wav",
                "file:///home/furnix/resources/Animals/Animals2/AnimalsSounds/hippo.wav", 
                "file:///home/furnix/resources/Animals/Animals2/AnimalsSounds/horse.wav",
                "file:///home/furnix/resources/Animals/Animals2/AnimalsSounds/lion.wav", 
                "file:///home/furnix/resources/Animals/Animals2/AnimalsSounds/monkey.wav",
                "file:///home/furnix/resources/Animals/Animals2/AnimalsSounds/mouse.wav",
                "file:///home/furnix/resources/Animals/Animals2/AnimalsSounds/pig.wav",
                "file:///home/furnix/resources/Animals/Animals2/AnimalsSounds/sheep.wav",  
                "file:///home/furnix/resources/Animals/Animals2/AnimalsSounds/tiger.wav",
                "file:///home/furnix/resources/Animals/Animals2/AnimalsSounds/zebra.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
