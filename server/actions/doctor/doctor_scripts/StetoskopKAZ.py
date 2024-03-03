
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jane")
    
    url_list = ["http://novators.kz/audio/DoctorKAZ/StetoskopKAZ/StetoskopKAZ1.wav", "http://novators.kz/audio/DoctorKAZ/StetoskopKAZ/StetoskopKAZ2.wav", "http://novators.kz/audio/DoctorKAZ/StetoskopKAZ/StetoskopKAZ3.wav", "http://novators.kz/audio/DoctorKAZ/StetoskopKAZ/StetoskopKAZ4.wav", "http://novators.kz/audio/DoctorKAZ/StetoskopKAZ/StetoskopKAZ5.wav", "http://novators.kz/audio/DoctorKAZ/StetoskopKAZ/StetoskopKAZ6.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
