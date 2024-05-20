
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Chen")
    
    furhat.say(url="file:///home/furnix/resources/EnglishTeacherKAZ/mountain/16.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/EnglishTeacherKAZ/mountain/17.wav", lipsync=True)
