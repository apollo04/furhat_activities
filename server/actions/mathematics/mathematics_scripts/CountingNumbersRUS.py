
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/Counting/CountingRUS/CountingNumbersRUS/CountingRUS1.wav", "http://novators.kz/audio/Counting/CountingRUS/CountingNumbersRUS/CountingRUS2.wav", "http://novators.kz/audio/Counting/CountingRUS/CountingNumbersRUS/oneRUS.wav", "http://novators.kz/audio/Counting/CountingRUS/CountingNumbersRUS/twoRUS.wav", "http://novators.kz/audio/Counting/CountingRUS/CountingNumbersRUS/threeRUS.wav", "http://novators.kz/audio/Counting/CountingRUS/CountingNumbersRUS/fourRUS.wav", "http://novators.kz/audio/Counting/CountingRUS/CountingNumbersRUS/fiveRUS.wav", "http://novators.kz/audio/Counting/CountingRUS/CountingNumbersRUS/sixRUS.wav", "http://novators.kz/audio/Counting/CountingRUS/CountingNumbersRUS/sevenRUS.wav", "http://novators.kz/audio/Counting/CountingRUS/CountingNumbersRUS/eightRUS.wav", "http://novators.kz/audio/Counting/CountingRUS/CountingNumbersRUS/nineRUS.wav", "http://novators.kz/audio/Counting/CountingRUS/CountingNumbersRUS/tenRUS.wav", "http://novators.kz/audio/Counting/CountingRUS/CountingNumbersRUS/CountingRUS3.wav", "http://novators.kz/audio/Counting/CountingRUS/CountingNumbersRUS/CountingRUS4.wav", "http://novators.kz/audio/Counting/CountingRUS/CountingNumbersRUS/CountingRUS5.wav", "http://novators.kz/audio/Counting/CountingRUS/CountingNumbersRUS/CountingRUS6.wav", "http://novators.kz/audio/Counting/CountingRUS/CountingNumbersRUS/CountingRUS7.wav", "http://novators.kz/audio/Counting/CountingRUS/CountingNumbersRUS/CountingRUS8.wav", "http://novators.kz/audio/Counting/CountingRUS/CountingNumbersRUS/CountingRUS9.wav", "http://novators.kz/audio/Counting/CountingRUS/CountingNumbersRUS/CountingRUS10.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
