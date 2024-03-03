
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jane")
    
    url_list = ["http://novators.kz/audio/DoctorKAZ/ThermometerKAZ/ThermometerKAZ1.wav", "http://novators.kz/audio/DoctorKAZ/ThermometerKAZ/ThermometerKAZ2.wav", "http://novators.kz/audio/DoctorKAZ/ThermometerKAZ/ThermometerKAZ3.wav", "http://novators.kz/audio/DoctorKAZ/ThermometerKAZ/ThermometerKAZ4.wav", "http://novators.kz/audio/DoctorKAZ/ThermometerKAZ/ThermometerKAZ5.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
