
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Chen")
    
    furhat.say(url="file:///home/furnix/resources/EnglishTeacherKAZ/biggestCountry/18.wav", lipsync=True)
    time.sleep(15)
    furhat.say(url="file:///home/furnix/resources/EnglishTeacherKAZ/biggestCountry/18_1.wav", lipsync=True)
    
