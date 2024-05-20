
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jane")
    
    furhat.say(url="file:///home/furnix/resources/EnglishTeacherKAZ/globus/12.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/EnglishTeacherKAZ/globus/13.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/EnglishTeacherKAZ/globus/14.wav", lipsync=True)
    time.sleep(3)
    furhat.say(url="file:///home/furnix/resources/EnglishTeacherKAZ/globus/15.wav", lipsync=True)

