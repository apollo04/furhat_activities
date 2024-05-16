
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/DictantRUS/PraiseCorrectRUS/PraiseRUS1.wav", 
                "file:///home/furnix/resources/DictantRUS/PraiseCorrectRUS/PraiseRUS2.wav", 
                "file:///home/furnix/resources/DictantRUS/PraiseCorrectRUS/PraiseRUS3.wav", 
                "file:///home/furnix/resources/DictantRUS/PraiseCorrectRUS/PraiseRUS4.wav", 
                "file:///home/furnix/resources/DictantRUS/PraiseCorrectRUS/PraiseRUS5.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
