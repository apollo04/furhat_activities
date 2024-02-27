
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jane")
    
    url_list = ["http://novators.kz/audio/DoctorKAZ/IntroKAZ/IntroKAZ1.wav", "http://novators.kz/audio/DoctorKAZ/IntroKAZ/IntroKAZ2.wav", "http://novators.kz/audio/DoctorKAZ/IntroKAZ/IntroKAZ3.wav", "http://novators.kz/audio/DoctorKAZ/IntroKAZ/IntroKAZ4.wav", "http://novators.kz/audio/DoctorKAZ/IntroKAZ/IntroKAZ5.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
