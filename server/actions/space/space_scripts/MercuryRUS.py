
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="James")
    
    url_list = ["file:///home/furnix/resources/Space/SpaceRUS/MercuryRUS/mercuryRUS1.wav", 
                "file:///home/furnix/resources/Space/SpaceRUS/MercuryRUS/mercuryRUS2.wav", 
                "file:///home/furnix/resources/Space/SpaceRUS/MercuryRUS/endRUS.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
