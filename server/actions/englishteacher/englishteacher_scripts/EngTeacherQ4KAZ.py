
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Chen")
    
    furhat.say(url="file:///home/furnix/resources/EnglishTeacherKAZ/longestRiver/19.wav", lipsync=True)
