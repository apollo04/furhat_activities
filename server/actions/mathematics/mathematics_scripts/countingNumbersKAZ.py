
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["http://novators.kz/audio/Counting/CountingKAZ/CountingNumbersKAZ/CountingKAZ1.wav", "http://novators.kz/audio/Counting/CountingKAZ/CountingNumbersKAZ/CountingKAZ2.wav", "http://novators.kz/audio/Counting/CountingKAZ/CountingNumbersKAZ/oneKAZ.wav", "http://novators.kz/audio/Counting/CountingKAZ/CountingNumbersKAZ/twoKAZ.wav", "http://novators.kz/audio/Counting/CountingKAZ/CountingNumbersKAZ/threeKAZ.wav", "http://novators.kz/audio/Counting/CountingKAZ/CountingNumbersKAZ/fourKAZ.wav", "http://novators.kz/audio/Counting/CountingKAZ/CountingNumbersKAZ/fiveKAZ.wav", "http://novators.kz/audio/Counting/CountingKAZ/CountingNumbersKAZ/sixKAZ.wav", "http://novators.kz/audio/Counting/CountingKAZ/CountingNumbersKAZ/sevenKAZ.wav", "http://novators.kz/audio/Counting/CountingKAZ/CountingNumbersKAZ/eightKAZ.wav", "http://novators.kz/audio/Counting/CountingKAZ/CountingNumbersKAZ/nineKAZ.wav", "http://novators.kz/audio/Counting/CountingKAZ/CountingNumbersKAZ/tenKAZ.wav", "http://novators.kz/audio/Counting/CountingKAZ/CountingNumbersKAZ/CountingKAZ3.wav", "http://novators.kz/audio/Counting/CountingKAZ/CountingNumbersKAZ/CountingKAZ4.wav", "http://novators.kz/audio/Counting/CountingKAZ/CountingNumbersKAZ/CountingKAZ5.wav", "http://novators.kz/audio/Counting/CountingKAZ/CountingNumbersKAZ/CountingKAZ6.wav", "http://novators.kz/audio/Counting/CountingKAZ/CountingNumbersKAZ/CountingKAZ7.wav", "http://novators.kz/audio/Counting/CountingKAZ/CountingNumbersKAZ/CountingKAZ8.wav", "http://novators.kz/audio/Counting/CountingKAZ/CountingNumbersKAZ/CountingKAZ9.wav", "http://novators.kz/audio/Counting/CountingKAZ/CountingNumbersKAZ/CountingKAZ10.wav", "http://novators.kz/audio/Counting/CountingKAZ/CountingNumbersKAZ/CountingKAZ11.wav", "http://novators.kz/audio/Counting/CountingKAZ/CountingNumbersKAZ/CountingKAZ12.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
