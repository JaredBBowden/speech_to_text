import sys
#sys.path.insert(0, '/Users/Jared/Documents/speech_recognition/')
sys.path.insert(0, '../speech_recognition/')
import speech_recognition as sr
from os import path
import datetime

######################################################
# From microphone
######################################################
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))


######################################################
# From file
######################################################

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")

    # TODO Find a more dynamic recording method
    audio = r.record(source, duration=5)

# Build the filename
file_name = "./data/" + str(datetime.datetime.now()) + ".wav"

# Title with datetime
with open(file_name, "wb") as f:
    f.write(audio.get_wav_data())

AUDIO_FILE = file_name

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    the_text = r.recognize_sphinx(audio)
    
    # Add an extra line to parse timestamps
    the_time = r.recognize_sphinx(audio, show_all=True)
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

# Quick google example
r.recognize_google(audio)

# Can we pull the timestamps?
# https://stackoverflow.com/questions/37973541/segment-timestamps-in-pocketsphinx
[(seg.word, seg.start_frame, seg.end_frame) for seg in the_time.seg()]