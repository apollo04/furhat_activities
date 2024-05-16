
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/DictantKAZ/RabbitKAZ/Rabbit1.wav", 
                "file:///home/furnix/resources/DictantKAZ/RabbitKAZ/Rabbit2.wav", 
                "file:///home/furnix/resources/DictantKAZ/RabbitKAZ/Rabbit3.wav", 
                "file:///home/furnix/resources/DictantKAZ/RabbitKAZ/Rabbit4.wav", 
                "file:///home/furnix/resources/DictantKAZ/RabbitKAZ/Rabbit5.wav", 
                "file:///home/furnix/resources/DictantKAZ/RabbitKAZ/Rabbit6.wav", 
                "file:///home/furnix/resources/DictantKAZ/RabbitKAZ/Rabbit7.wav", 
                "file:///home/furnix/resources/DictantKAZ/RabbitKAZ/Rabbit8.wav", 
                "file:///home/furnix/resources/DictantKAZ/RabbitKAZ/Rabbit9.wav", 
                "file:///home/furnix/resources/DictantKAZ/RabbitKAZ/Rabbit10.wav", 
                "file:///home/furnix/resources/DictantKAZ/RabbitKAZ/Rabbit11.wav", 
                "file:///home/furnix/resources/DictantKAZ/RabbitKAZ/Rabbit12.wav", 
                "file:///home/furnix/resources/DictantKAZ/RabbitKAZ/Rabbit13.wav", 
                "file:///home/furnix/resources/DictantKAZ/RabbitKAZ/Rabbit14.wav", 
                "file:///home/furnix/resources/DictantKAZ/RabbitKAZ/Rabbit15.wav", 
                "file:///home/furnix/resources/DictantKAZ/RabbitKAZ/Rabbit16.wav", 
                "file:///home/furnix/resources/DictantKAZ/RabbitKAZ/Rabbit17.wav", 
                "file:///home/furnix/resources/DictantKAZ/RabbitKAZ/Rabbit18.wav", 
                "file:///home/furnix/resources/DictantKAZ/RabbitKAZ/Rabbit19.wav", 
                "file:///home/furnix/resources/DictantKAZ/RabbitKAZ/Rabbit20.wav", 
                "file:///home/furnix/resources/DictantKAZ/RabbitKAZ/Rabbit21.wav", 
                "file:///home/furnix/resources/DictantKAZ/RabbitKAZ/Rabbit22.wav", 
                "file:///home/furnix/resources/DictantKAZ/RabbitKAZ/Rabbit23.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
