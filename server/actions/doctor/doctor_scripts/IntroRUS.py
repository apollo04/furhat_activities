
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jane")
    
    url_list = ["file:///home/furnix/resources/DoctorRUS/IntroRUS/IntroRUS1_n.wav", 
                "file:///home/furnix/resources/DoctorRUS/IntroRUS/IntroRUS2_n.wav", 
                "file:///home/furnix/resources/DoctorRUS/IntroRUS/IntroRUS3_n.wav", 
                "file:///home/furnix/resources/DoctorRUS/IntroRUS/IntroRUS4_n.wav", 
                "file:///home/furnix/resources/DoctorRUS/IntroRUS/IntroRUS5_n.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
