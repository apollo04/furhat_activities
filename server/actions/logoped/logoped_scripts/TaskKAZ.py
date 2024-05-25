
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Isabel")
    
    url_list = ["file:///home/furnix/resources/LogopedKAZ/TaskKAZ/TaskKAZ1.wav", 
                "file:///home/furnix/resources/LogopedKAZ/TaskKAZ/TaskKAZ2.wav", 
                "file:///home/furnix/resources/LogopedKAZ/TaskKAZ/TaskKAZ3.wav", 
                "file:///home/furnix/resources/LogopedKAZ/TaskKAZ/TaskKAZ4.wav", 
                "file:///home/furnix/resources/LogopedKAZ/TaskKAZ/TaskKAZ5.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
