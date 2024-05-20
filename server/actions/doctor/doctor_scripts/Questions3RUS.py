from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="Jane")
    

    furhat.say(url="file:///home/furnix/resources/DoctorRUS/QuestionsRUS/QuestionsRUS3_n.wav", lipsync=True)