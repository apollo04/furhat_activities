
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Alex")
    
    url_list = ["file:///home/furnix/resources/SuperheroesRUS/BatmanRUS/Batman1.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/BatmanRUS/Batman4.wav", 
                "file:///home/furnix/resources/SuperheroesRUS/BatmanRUS/Batman5.wav" 
                ]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
    furhat.say(url="file:///home/furnix/resources/SuperheroesRUS/BatmanRUS/Batman2.wav", lipsync=True)
    time.sleep(5)
    furhat.say(url="file:///home/furnix/resources/SuperheroesRUS/BatmanRUS/Batman3.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/SuperheroesRUS/BatmanRUS/Batman6.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/SuperheroesRUS/BatmanRUS/Batman7.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/SuperheroesRUS/BatmanRUS/Batman9.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/SuperheroesRUS/BatmanRUS/Batman10.wav", lipsync=True)


