
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Chen")
    
    furhat.say(url="file:///home/furnix/resources/EnglishTeacherKAZ/age/5.wav", lipsync=True)
    time.sleep(7)
    furhat.say(url="file:///home/furnix/resources/EnglishTeacherKAZ/globus/6.wav", lipsync=True)
    time.sleep(3)
    furhat.say(url="file:///home/furnix/resources/EnglishTeacherKAZ/globus/7.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/EnglishTeacherKAZ/globus/8.wav", lipsync=True)
    time.sleep(3)
    furhat.say(url="file:///home/furnix/resources/EnglishTeacherKAZ/globus/9.wav", lipsync=True)
    time.sleep(3)
    furhat.say(url="file:///home/furnix/resources/EnglishTeacherKAZ/globus/10.wav", lipsync=True)
    

