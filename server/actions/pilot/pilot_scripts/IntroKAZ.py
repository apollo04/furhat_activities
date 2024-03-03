
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jamie")
    
    url_list = ["http://novators.kz/audio/PilotKAZ/IntroKAZ/IntroKAZ1.wav",    "http://novators.kz/audio/PilotKAZ/IntroKAZ/IntroKAZ2.wav",
         "http://novators.kz/audio/PilotKAZ/PilotInfoKAZ/pilotInfoKAZ2.wav", "http://novators.kz/audio/PilotKAZ/PilotInfoKAZ/pilotInfoKAZ3.wav", "http://novators.kz/audio/PilotKAZ/PilotInfoKAZ/pilotInfoKAZ4.wav", "http://novators.kz/audio/PilotKAZ/PilotInfoKAZ/pilotInfoKAZ5.wav", "http://novators.kz/audio/PilotKAZ/PilotInfoKAZ/pilotInfoKAZ6.wav",
             "http://novators.kz/audio/PilotKAZ/PilotInfoKAZ/pilotInfoKAZ1.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
