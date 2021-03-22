"# speech_recognition" 

Instructions :

create an API KEY and save it to in .json file renaming it to api-key.json.

run python setup.py // to download all the neccessary files for speech recognition api.

then run : 
  pip install -r requirements.txt
  
To use speech_recognition.py.

import transcribe # from speech recognition py file

import speech_recognition as sr

tr = transcribe("path_to_audio_file" , sr)

text = tr.run_recognizer(tr.recognizer.recognize_google_cloud(credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS \
enable_automatic_punctuation=True #can add more functions call ))
