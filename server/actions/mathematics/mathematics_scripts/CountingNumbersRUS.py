
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/Counting/CountingRUS/CountingNumbersRUS/CountingRUS1.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/CountingNumbersRUS/CountingRUS2.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/CountingNumbersRUS/oneRUS.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/CountingNumbersRUS/twoRUS.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/CountingNumbersRUS/threeRUS.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/CountingNumbersRUS/fourRUS.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/CountingNumbersRUS/fiveRUS.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/CountingNumbersRUS/sixRUS.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/CountingNumbersRUS/sevenRUS.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/CountingNumbersRUS/eightRUS.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/CountingNumbersRUS/nineRUS.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/CountingNumbersRUS/tenRUS.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/CountingNumbersRUS/CountingRUS3.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/CountingNumbersRUS/CountingRUS4.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/CountingNumbersRUS/CountingRUS5.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/CountingNumbersRUS/CountingRUS6.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/CountingNumbersRUS/CountingRUS7.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/CountingNumbersRUS/CountingRUS8.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/CountingNumbersRUS/CountingRUS9.wav", 
                "file:///home/furnix/resources/Counting/CountingRUS/CountingNumbersRUS/CountingRUS10.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
        time.sleep(10)
