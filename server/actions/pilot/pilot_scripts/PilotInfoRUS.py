
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jamie")
    
    url_list = ["http://novators.kz/audio/PilotRUS/PilotInfoRUS/PilotInfoRUS1.wav", "http://novators.kz/audio/PilotRUS/PilotInfoRUS/PilotInfoRUS2.wav", "http://novators.kz/audio/PilotRUS/PilotInfoRUS/PilotInfoRUS3.wav", "http://novators.kz/audio/PilotRUS/PilotInfoRUS/PilotInfoRUS4.wav", "http://novators.kz/audio/PilotRUS/PilotInfoRUS/PilotInfoRUS5.wav", "http://novators.kz/audio/PilotRUS/PilotInfoRUS/PilotInfoRUS6.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
