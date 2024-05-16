
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jane")
    
    url_list = ["file:///home/furnix/resources/DoctorRUS/QuestionsRUS/QuestionsRUS1_n.wav",
                "file:///home/furnix/resources/DoctorRUS/QuestionsRUS/QuestionsRUS2_n.wav",
                "file:///home/furnix/resources/DoctorRUS/QuestionsRUS/QuestionsRUS3_n.wav",
                "file:///home/furnix/resources/DoctorRUS/QuestionsRUS/QuestionsRUS4_n.wav",
                "file:///home/furnix/resources/DoctorRUS/QuestionsRUS/QuestionsRUS5_n.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
