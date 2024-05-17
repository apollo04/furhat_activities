import random 
import sys
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Samuel")
    
    url_list = ["file:///home/furnix/resources/Animals/Animals2/AnimalsKAZ/animalsEnding1KAZ.wav",
                "file:///home/furnix/resources/Animals/Animals2/AnimalsKAZ/animalsEnding2KAZ.wav",
                "file:///home/furnix/resources/Animals/Animals2/AnimalsKAZ/animalsEnding3KAZ.wav"
                ]

    random_url = random.choice(url_list)
    furhat.say(url=random_url, lipsync=True)
    time.sleep(5)
    furhat.say(url="file:///home/furnix/resources/Animals/Animals2/AnimalsKAZ/animalsEveryEnding2KAZ.wav", lipsync=True)