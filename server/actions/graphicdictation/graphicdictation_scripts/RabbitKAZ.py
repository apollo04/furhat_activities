
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/DictantKAZ/RabbitKAZ/Rabbit1.wav", "http://novators.kz/audio/DictantKAZ/RabbitKAZ/Rabbit2.wav", "http://novators.kz/audio/DictantKAZ/RabbitKAZ/Rabbit3.wav", "http://novators.kz/audio/DictantKAZ/RabbitKAZ/Rabbit4.wav", "http://novators.kz/audio/DictantKAZ/RabbitKAZ/Rabbit5.wav", "http://novators.kz/audio/DictantKAZ/RabbitKAZ/Rabbit6.wav", "http://novators.kz/audio/DictantKAZ/RabbitKAZ/Rabbit7.wav", "http://novators.kz/audio/DictantKAZ/RabbitKAZ/Rabbit8.wav", "http://novators.kz/audio/DictantKAZ/RabbitKAZ/Rabbit9.wav", "http://novators.kz/audio/DictantKAZ/RabbitKAZ/Rabbit10.wav", "http://novators.kz/audio/DictantKAZ/RabbitKAZ/Rabbit11.wav", "http://novators.kz/audio/DictantKAZ/RabbitKAZ/Rabbit12.wav", "http://novators.kz/audio/DictantKAZ/RabbitKAZ/Rabbit13.wav", "http://novators.kz/audio/DictantKAZ/RabbitKAZ/Rabbit14.wav", "http://novators.kz/audio/DictantKAZ/RabbitKAZ/Rabbit15.wav", "http://novators.kz/audio/DictantKAZ/RabbitKAZ/Rabbit16.wav", "http://novators.kz/audio/DictantKAZ/RabbitKAZ/Rabbit17.wav", "http://novators.kz/audio/DictantKAZ/RabbitKAZ/Rabbit18.wav", "http://novators.kz/audio/DictantKAZ/RabbitKAZ/Rabbit19.wav", "http://novators.kz/audio/DictantKAZ/RabbitKAZ/Rabbit20.wav", "http://novators.kz/audio/DictantKAZ/RabbitKAZ/Rabbit21.wav", "http://novators.kz/audio/DictantKAZ/RabbitKAZ/Rabbit22.wav", "http://novators.kz/audio/DictantKAZ/RabbitKAZ/Rabbit23.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
