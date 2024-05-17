import random 
import sys
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Patricia")
    
    url_list = ["file:///home/furnix/resources/Animals/Animals2/AnimalsRUS/animalsEnding1RUS.wav",
                "file:///home/furnix/resources/Animals/Animals2/AnimalsRUS/animalsEnding2RUS.wav",
                "file:///home/furnix/resources/Animals/Animals2/AnimalsRUS/animalsEnding3RUS.wav"
                ]
    random_url = random.choice(url_list)
    furhat.say(url=random_url, lipsync=True)
    time.sleep(5)
    furhat.say(url="file:///home/furnix/resources/Animals/Animals2/AnimalsRUS/animalsEveryEnding2RUS.wav", lipsync=True)

   