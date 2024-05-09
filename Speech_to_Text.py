import speech_recognition as sr
import wave
import pyaudio
from google.cloud import speech
import Text_to_Speech
def spch_to_txt():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Talk")
        Text_to_Speech.spk("Talk")
        #r.pause_threshold = 4
        audio_text = r.listen(source)
        print("Time over, thanks")
        Text_to_Speech.spk("Time over, thanks")
    output_file = "output.wav"
    with wave.open(output_file, "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
        f.setframerate(50000)
        f.writeframes(audio_text.get_wav_data())
    try:
        print("Text is : "+r.recognize_google(audio_text))
        Text_to_Speech.spk("Query is : "+r.recognize_google(audio_text))
        x = ""
        x = r.recognize_google(audio_text)
        print(x)
        return x
    except sr.UnknownValueError:
        Text_to_Speech.spk("Unable to recognize speech, Speak again")
        spch_to_txt()
#spch_to_txt()
    