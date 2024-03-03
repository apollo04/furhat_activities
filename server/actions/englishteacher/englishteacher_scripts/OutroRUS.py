
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jane")
    
    url_list = ["http://novators.kz/audio/EngTeacherRUS/OutroRUS/OutroRUS1.wav", "http://novators.kz/audio/EngTeacherRUS/OutroRUS/OutroENG1.wav", "http://novators.kz/audio/EngTeacherRUS/OutroRUS/OutroRUS2.wav", "http://novators.kz/audio/EngTeacherRUS/OutroRUS/OutroENG2.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
