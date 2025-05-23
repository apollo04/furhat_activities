
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jane")
    
    url_list = ["file:///home/furnix/resources/DoctorRUS/StetoskopRUS/StetoskopRUS1_n.wav", 
                "file:///home/furnix/resources/DoctorRUS/StetoskopRUS/StetoskopRUS2_n.wav", 
                "file:///home/furnix/resources/DoctorRUS/StetoskopRUS/StetoskopRUS3_n.wav", 
                "file:///home/furnix/resources/DoctorRUS/StetoskopRUS/StetoskopRUS4_n.wav", 
                "file:///home/furnix/resources/DoctorRUS/StetoskopRUS/StetoskopRUS5_n.wav"]

    furhat.say(url="file:///home/furnix/resources/DoctorRUS/StetoskopRUS/StetoskopRUS1_n.wav", lipsync=True)
    time.sleep(3)
    furhat.say(url="file:///home/furnix/resources/DoctorRUS/StetoskopRUS/StetoskopRUS5_n.wav", lipsync=True)

