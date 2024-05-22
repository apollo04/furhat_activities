from furhat_remote_api import FurhatRemoteAPI
import time
import json

def lip_sync_gesture():
     with open('/Users/Master/Desktop/offline_hri/server/actions/lip_sync_gesture.json', 'r') as file:
        gesture_data = json.load(file)
        return gesture_data

def perform_gesture(furhat):
    furhat.gesture(body = lip_sync_gesture())

def perform_lip_sync(furhat: FurhatRemoteAPI, audio_duration: float, audio_file: str):
    # Start the audio playback
    #furhat.say(url="audio_file", lipsync=True)
    furhat.say(url = audio_file, lipsync=True)

    # Perform gestures while the audio is playing
    start_time = time.time()
    while time.time() - start_time < audio_duration:
        perform_gesture(furhat)
        time.sleep(0.5)  # Adjust the sleep time as necessary to control the frequency of gestures



