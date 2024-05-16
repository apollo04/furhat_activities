
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/DictantKAZ/ElephantKAZ/Elephant1.wav", 
                "file:///home/furnix/resources/DictantKAZ/ElephantKAZ/Elephant2.wav", 
                "file:///home/furnix/resources/DictantKAZ/ElephantKAZ/Elephant3.wav", 
                "file:///home/furnix/resources/DictantKAZ/ElephantKAZ/Elephant4.wav", 
                "file:///home/furnix/resources/DictantKAZ/ElephantKAZ/Elephant5.wav", 
                "file:///home/furnix/resources/DictantKAZ/ElephantKAZ/Elephant6.wav", 
                "file:///home/furnix/resources/DictantKAZ/ElephantKAZ/Elephant7.wav", 
                "file:///home/furnix/resources/DictantKAZ/ElephantKAZ/Elephant8.wav", 
                "file:///home/furnix/resources/DictantKAZ/ElephantKAZ/Elephant9.wav", 
                "file:///home/furnix/resources/DictantKAZ/ElephantKAZ/Elephant10.wav", 
                "file:///home/furnix/resources/DictantKAZ/ElephantKAZ/Elephant11.wav", 
                "file:///home/furnix/resources/DictantKAZ/ElephantKAZ/Elephant12.wav", 
                "file:///home/furnix/resources/DictantKAZ/ElephantKAZ/Elephant13.wav", 
                "file:///home/furnix/resources/DictantKAZ/ElephantKAZ/Elephant14.wav", 
                "file:///home/furnix/resources/DictantKAZ/ElephantKAZ/Elephant15.wav", 
                "file:///home/furnix/resources/DictantKAZ/ElephantKAZ/Elephant16.wav", 
                "file:///home/furnix/resources/DictantKAZ/ElephantKAZ/Elephant17.wav", 
                "file:///home/furnix/resources/DictantKAZ/ElephantKAZ/Elephant18.wav", 
                "file:///home/furnix/resources/DictantKAZ/ElephantKAZ/Elephant19.wav", 
                "file:///home/furnix/resources/DictantKAZ/ElephantKAZ/Elephant20.wav", 
                "file:///home/furnix/resources/DictantKAZ/ElephantKAZ/Elephant21.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
