
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jane")
    
    url_list = ["http://novators.kz/audio/DoctorRUS/ShpritzRUS/ShpritzRUS1.wav", "http://novators.kz/audio/DoctorRUS/ShpritzRUS/ShpritzRUS2.wav", "http://novators.kz/audio/DoctorRUS/ShpritzRUS/ShpritzRUS3.wav", "http://novators.kz/audio/DoctorRUS/ShpritzRUS/ShpritzRUS4.wav", "http://novators.kz/audio/DoctorRUS/ShpritzRUS/ShpritzRUS5.wav", "http://novators.kz/audio/DoctorRUS/ShpritzRUS/ShpritzRUS6.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
