
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jane")
    
    url_list = ["http://novators.kz/audio/DoctorRUS/ShpatelRUS/ShpatelRUS1.wav", "http://novators.kz/audio/DoctorRUS/ShpatelRUS/ShpatelRUS2.wav", "http://novators.kz/audio/DoctorRUS/ShpatelRUS/ShpatelRUS3.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
