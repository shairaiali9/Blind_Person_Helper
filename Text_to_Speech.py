import pyttsx3  
from pyttsx3 import init
import Speech_to_Text
# initialize Text-to-speech engine  
engine = pyttsx3.init()  
def start():
    # convert this text to speech  
    engine.say("What can I help?, Read text, Summarize recognitioned text, Detect objects and Seen explanation")
    engine.setProperty("rate", 100)  
    #engine.say(text)  
    # play the speech  
    engine.runAndWait()
def rt(text):
    
    ch = ""
    ch = Speech_to_Text.spch_to_txt()
    if ch == "yes":
        read_text(text)
    elif ch == "no":
        engine.say("Okay.")
    else:
        engine.say("Speak again.")
        rt(text)
        

def read_text(text):
    #text = r"""pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3."""
    engine.setProperty("rate", 200)  
    engine.say(text)  
    # play the speech  
    engine.say("Have to read again? Yes or No?")
    rt(text)    
    engine.runAndWait() 

def spk(text):
    engine.say(text)
    engine.setProperty("rate", 200)  
    #engine.say(text)  
    # play the speech  
    engine.runAndWait() 