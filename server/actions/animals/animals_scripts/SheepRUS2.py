
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Patricia")
    
    url_list = ["file:///home/furnix/resources/Animals/Animals2/AnimalsRUS/SheepRUS/SheepRUS2.wav",
                "file:///home/furnix/resources/Animals/Animals2/AnimalsRUS/animalsEnding1RUS.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
