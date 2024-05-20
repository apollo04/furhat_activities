
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="James")

    furhat.say(url="file:///home/furnix/resources/Space/SpaceKAZ/EarthKAZ/earthKAZ1.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/Space/SpaceKAZ/EarthKAZ/earthKAZ2.wav", lipsync=True)
    
    

