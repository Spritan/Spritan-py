# importing the pyttsx library
import pyttsx3
# import pyaudio

# initialisation
engine = pyttsx3.init()

# testing

#    engine.say("My first code on text-to-speech")
#    engine.runAndWait()

# function

def speak_it (op):
    engine.say(op)
    engine.runAndWait()
