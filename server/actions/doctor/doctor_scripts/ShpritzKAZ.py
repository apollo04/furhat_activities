
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jane")
    
    url_list = ["file:///home/furnix/resources/DoctorKAZ/ShpritzKAZ/ShpritzKAZ1_n.wav", 
                "file:///home/furnix/resources/DoctorKAZ/ShpritzKAZ/ShpritzKAZ2_n.wav", 
                "file:///home/furnix/resources/DoctorKAZ/ShpritzKAZ/ShpritzKAZ3_n.wav", 
                "file:///home/furnix/resources/DoctorKAZ/ShpritzKAZ/ShpritzKAZ4_n.wav", 
                "file:///home/furnix/resources/DoctorKAZ/ShpritzKAZ/ShpritzKAZ5_n.wav", 
                "file:///home/furnix/resources/DoctorKAZ/ShpritzKAZ/ShpritzKAZ6_n.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
