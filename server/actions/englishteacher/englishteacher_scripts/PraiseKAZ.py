
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jane")
    
    furhat.say(url="file:///home/furnix/resources/EnglishTeacherKAZ/success/11.wav", lipsync=True)
