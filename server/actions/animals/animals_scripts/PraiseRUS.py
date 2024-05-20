
import random
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Patricia")

    url_list = ["file:///home/furnix/resources/Animals/Animals2/AnimalsRUS/PraiseRUS/animalsPraiseRUS1.wav",
                "file:///home/furnix/resources/Animals/Animals2/AnimalsRUS/PraiseRUS/animalsPraiseRUS2.wav"
                ]
    
    random_url = random.choice(url_list)
    furhat.say(url=random_url, lipsync=True)