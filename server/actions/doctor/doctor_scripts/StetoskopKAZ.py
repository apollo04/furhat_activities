
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jane")
    
    url_list = ["file:///home/furnix/resources/DoctorKAZ/StetoskopKAZ/StetoskopKAZ1_n.wav", 
                "file:///home/furnix/resources/DoctorKAZ/StetoskopKAZ/StetoskopKAZ2_n.wav", 
                "file:///home/furnix/resources/DoctorKAZ/StetoskopKAZ/StetoskopKAZ3_n.wav", 
                "file:///home/furnix/resources/DoctorKAZ/StetoskopKAZ/StetoskopKAZ4_n.wav", 
                "file:///home/furnix/resources/DoctorKAZ/StetoskopKAZ/StetoskopKAZ5_n.wav", 
                "file:///home/furnix/resources/DoctorKAZ/StetoskopKAZ/StetoskopKAZ6_n.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
