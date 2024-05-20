
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="James")
   
    furhat.say(url="file:///home/furnix/resources/Space/SpaceKAZ/JupiterKAZ/endKAZ.wav", lipsync=True)