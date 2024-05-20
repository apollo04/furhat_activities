
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")

    furhat.say(url="file:///home/furnix/resources/HolidaysRUS/NewYearRUS/NewYearRUS1_n.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/HolidaysRUS/NewYearRUS/NewYearRUS2_n.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/HolidaysRUS/NewYearRUS/NewYearRUS3_n.wav", lipsync=True)
    time.sleep(1)
    furhat.say(url="file:///home/furnix/resources/HolidaysRUS/NewYearRUS/NewYearRUS4_n.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/HolidaysRUS/NewYearRUS/NewYearRUS5_n.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/HolidaysRUS/NewYearRUS/NewYearRUS6_n.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/HolidaysRUS/NewYearRUS/NewYearRUS7_n.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/HolidaysRUS/NewYearRUS/NewYearRUS8_n.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/HolidaysRUS/NewYearRUS/NewYearRUS9_n.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/HolidaysRUS/NewYearRUS/NewYearRUS10_n.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/HolidaysRUS/NewYearRUS/NewYearRUS11_n.wav", lipsync=True)
    time.sleep(2)
    furhat.say(url="file:///home/furnix/resources/HolidaysRUS/NewYearRUS/NewYearRUS13_n.wav", lipsync=True)
    time.sleep(15)
    furhat.say(url="file:///home/furnix/resources/HolidaysRUS/NewYearRUS/NewYearRUS14_n.wav", lipsync=True)
        
    
