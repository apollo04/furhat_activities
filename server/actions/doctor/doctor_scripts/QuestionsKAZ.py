
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jane")
    
    url_list = ["file:///home/furnix/resources/DoctorKAZ/QuestionsKAZ/QuestionsKAZ1_n.wav",
                "file:///home/furnix/resources/DoctorKAZ/QuestionsKAZ/QuestionsKAZ2_n.wav",
                "file:///home/furnix/resources/DoctorKAZ/QuestionsKAZ/QuestionsKAZ3_n.wav",
                "file:///home/furnix/resources/DoctorKAZ/QuestionsKAZ/QuestionsKAZ4_n.wav",
                "file:///home/furnix/resources/DoctorKAZ/QuestionsKAZ/QuestionsKAZ5_n.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
