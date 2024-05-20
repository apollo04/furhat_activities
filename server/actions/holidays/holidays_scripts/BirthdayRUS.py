
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")

    furhat.say(url="file:///home/furnix/resources/HolidaysRUS/BirthdayRUS/BirthdayRUS1_n.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/HolidaysRUS/BirthdayRUS/BirthdayRUS2_n.wav", lipsync=True)
    time.sleep(20)
    furhat.say(url="file:///home/furnix/resources/HolidaysRUS/BirthdayRUS/BirthdayRUS3_n.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/HolidaysRUS/BirthdayRUS/BirthdayRUS4_n.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/HolidaysRUS/BirthdayRUS/BirthdayRUS5_n.wav", lipsync=True)
    time.sleep(15)
    furhat.say(url="file:///home/furnix/resources/HolidaysRUS/BirthdayRUS/BirthdayRUS6_n.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/HolidaysRUS/BirthdayRUS/BirthdayRUS7_n.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/HolidaysRUS/BirthdayRUS/BirthdayRUS8_n.wav", lipsync=True)
    time.sleep(5)
    furhat.say(url="file:///home/furnix/resources/HolidaysRUS/BirthdayRUS/BirthdayRUS10_n.wav", lipsync=True)
    time.sleep(5)
    furhat.say(url="file:///home/furnix/resources/HolidaysRUS/BirthdayRUS/BirthdayRUS11_n.wav", lipsync=True)





