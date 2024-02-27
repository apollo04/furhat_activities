
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jane")
    
    url_list = ["http://novators.kz/audio/DoctorKAZ/ShpritzKAZ/ShpritzKAZ1.wav", "http://novators.kz/audio/DoctorKAZ/ShpritzKAZ/ShpritzKAZ2.wav", "http://novators.kz/audio/DoctorKAZ/ShpritzKAZ/ShpritzKAZ3.wav", "http://novators.kz/audio/DoctorKAZ/ShpritzKAZ/ShpritzKAZ4.wav", "http://novators.kz/audio/DoctorKAZ/ShpritzKAZ/ShpritzKAZ5.wav", "http://novators.kz/audio/DoctorKAZ/ShpritzKAZ/ShpritzKAZ6.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
