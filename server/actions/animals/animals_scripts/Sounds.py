
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yi")
    
    url_list = ["http://novators.kz/audio/Animals/Animals2/AnimalsSounds/cat.wav", "http://novators.kz/audio/Animals/Animals2/AnimalsSounds/cow.wav", "http://novators.kz/audio/Animals/Animals2/AnimalsSounds/cat.wav", "http://novators.kz/audio/Animals/Animals2/AnimalsSounds/dog.wav", "http://novators.kz/audio/Animals/Animals2/AnimalsSounds/elephant.wav", "http://novators.kz/audio/Animals/Animals2/AnimalsSounds/frog.wav", "http://novators.kz/audio/Animals/Animals2/AnimalsSounds/horse.wav", "http://novators.kz/audio/Animals/Animals2/AnimalsSounds/monkey.wav", "http://novators.kz/audio/Animals/Animals2/AnimalsSounds/sheep.wav", "http://novators.kz/audio/Animals/Animals2/AnimalsSounds/squirrel.wav", "http://novators.kz/audio/Animals/Animals2/AnimalsSounds/tiger.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
