
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Chen")
    
   
    furhat.say(url="file:///home/furnix/resources/EnglishTeacherKAZ/IntroAndName/1.wav", lipsync=True)
    time.sleep(3)
    furhat.say(url="file:///home/furnix/resources/EnglishTeacherKAZ/IntroAndName/2.wav", lipsync=True)
    time.sleep(3)
    furhat.say(url="file:///home/furnix/resources/EnglishTeacherKAZ/IntroAndName/3.wav", lipsync=True)
    time.sleep(15)
    furhat.say(url="file:///home/furnix/resources/EnglishTeacherKAZ/IntroAndName/4.wav", lipsync=True)
