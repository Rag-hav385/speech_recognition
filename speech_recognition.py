
#Making the api-key for google speech_recognition and getting the credentials
with open("api-key.json") as f:
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = f.read()

# from SpeechRecognition package, import speech_recognition module
# https://github.com/Uberi/speech_recognition#readme
import speech_recognition as sr

class transcribe:

    def __init__(self , path_to_audio_file , sr):

        self.recognizer = sr.Recognizer()
        with sr.AudioFile(path_to_audio_file) as source:
            self.audio = r.record(source)

    def run_recognizer(self , r):

        #Can add functionalities to r when called in any manner.

        text = r()(self.audio)

        return text

#Sample call :

"""
tr = transcribe("/audio_file" , sr)
text = tr.run_recognizer(tr.recognizer.recognize_google_cloud(credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS \
enable_automatic_punctuation=True #can add more functions call ))
print(text)
"""
