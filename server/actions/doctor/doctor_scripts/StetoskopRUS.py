
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jane")
    
    url_list = ["http://novators.kz/audio/DoctorRUS/StetoskopRUS/StetoskopRUS1.wav", "http://novators.kz/audio/DoctorRUS/StetoskopRUS/StetoskopRUS2.wav", "http://novators.kz/audio/DoctorRUS/StetoskopRUS/StetoskopRUS3.wav", "http://novators.kz/audio/DoctorRUS/StetoskopRUS/StetoskopRUS4.wav", "http://novators.kz/audio/DoctorRUS/StetoskopRUS/StetoskopRUS5.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
