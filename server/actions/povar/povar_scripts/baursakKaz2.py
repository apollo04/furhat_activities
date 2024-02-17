import sys
import time

from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Rania")

    url_list = [
        'https://s3-eu-west-1.amazonaws.com/furhat-users/1618bde5-21db-46f6-b53c-d05a4bf14158/audio/cook-baursak-1-KAZ.wav',
        'https://s3-eu-west-1.amazonaws.com/furhat-users/1618bde5-21db-46f6-b53c-d05a4bf14158/audio/cook-baursak-2-KAZ.wav',
        'https://s3-eu-west-1.amazonaws.com/furhat-users/1618bde5-21db-46f6-b53c-d05a4bf14158/audio/cook-baursak-3-KAZ.wav',
        'https://s3-eu-west-1.amazonaws.com/furhat-users/1618bde5-21db-46f6-b53c-d05a4bf14158/audio/cook-baursak-4-KAZ.wav',
        'https://s3-eu-west-1.amazonaws.com/furhat-users/1618bde5-21db-46f6-b53c-d05a4bf14158/audio/cook-baursak-5-KAZ.wav',
        'https://s3-eu-west-1.amazonaws.com/furhat-users/1618bde5-21db-46f6-b53c-d05a4bf14158/audio/cook-baursak-6-KAZ.wav',
        'https://s3-eu-west-1.amazonaws.com/furhat-users/1618bde5-21db-46f6-b53c-d05a4bf14158/audio/cook-baursak-7-KAZ.wav',
        'https://s3-eu-west-1.amazonaws.com/furhat-users/1618bde5-21db-46f6-b53c-d05a4bf14158/audio/cook-baursak-8-KAZ.wav',
        'https://s3-eu-west-1.amazonaws.com/furhat-users/1618bde5-21db-46f6-b53c-d05a4bf14158/audio/cook-baursak-9-KAZ.wav',
        'https://s3-eu-west-1.amazonaws.com/furhat-users/1618bde5-21db-46f6-b53c-d05a4bf14158/audio/cook-baursak-10-KAZ.wav',
        'https://s3-eu-west-1.amazonaws.com/furhat-users/1618bde5-21db-46f6-b53c-d05a4bf14158/audio/cook-baursak-11-KAZ.wav',
    ]

    for url in url_list:
        furhat.say(url=url, lipsync=True)
