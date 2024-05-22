import sys
import os
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    # Initialize the Furhat SDK
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Omar")

    # Adjust the path to include the root 'actions' directory
    actions_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    if actions_path not in sys.path:
        sys.path.append(actions_path)

    # Import the custom gestures module
    from customGesture import perform_lip_sync

    # List of URLs to play
    url_list = [
        "file:///home/furnix/resources/Animals/Animals2/AnimalsKAZ/animalsIntro1KAZ.wav",
        "file:///home/furnix/resources/Animals/Animals2/AnimalsKAZ/animalsIntro2KAZ.wav"
    ]

    # Perform lip sync for each URL
    for url in url_list:
        perform_lip_sync(furhat, 30, url)

# Run the action with the provided IP address
run_action("10.101.17.184")
