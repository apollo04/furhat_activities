
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Yumi")
    
    url_list = ["file:///home/furnix/resources/HolidaysKAZ/KozheKAZ/Kozhe1_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/KozheKAZ/Kozhe2_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/KozheKAZ/Kozhe3_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/KozheKAZ/Kozhe4_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/KozheKAZ/Kozhe5_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/KozheKAZ/Kozhe6_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/KozheKAZ/Kozhe7_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/KozheKAZ/Kozhe8_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/KozheKAZ/Kozhe9_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/KozheKAZ/Kozhe10_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/KozheKAZ/Kozhe11_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/KozheKAZ/Kozhe12_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/KozheKAZ/Kozhe13_n.wav", 
                "file:///home/furnix/resources/HolidaysKAZ/KozheKAZ/Kozhe14_n.wav"]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
