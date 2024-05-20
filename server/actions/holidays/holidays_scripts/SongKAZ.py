
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    furhat.say(url="file:///home/furnix/resources/HolidaysKAZ/SongKAZ/Song1_n.wav", lipsync=True)
    furhat.say(url="file:///home/furnix/resources/HolidaysKAZ/SongKAZ/Song2_n.wav", lipsync=True)
    time.sleep(5)
    furhat.say(url="file:///home/furnix/resources/HolidaysKAZ/SongKAZ/Song3_n.wav", lipsync=True)
