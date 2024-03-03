
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jane")
    
    url_list = ["http://novators.kz/audio/DoctorRUS/OutroRUS/OutroRUS1.wav", "http://novators.kz/audio/DoctorRUS/OutroRUS/OutroRUS2.wav", "http://novators.kz/audio/DoctorRUS/OutroRUS/OutroRUS3.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
