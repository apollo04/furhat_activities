
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jane")
    
    url_list = ["http://novators.kz/audio/DoctorRUS/TermometerRUS/TermometerRUS1.wav", "http://novators.kz/audio/DoctorRUS/TermometerRUS/TermometerRUS2.wav", "http://novators.kz/audio/DoctorRUS/TermometerRUS/TermometerRUS3.wav", "http://novators.kz/audio/DoctorRUS/TermometerRUS/TermometerRUS4.wav", "http://novators.kz/audio/DoctorRUS/TermometerRUS/TermometerRUS5.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
