import speech_recognition
import pyaudio
import pyttsx3
import sys
import winsound
import os
import pyjokes
r = speech_recognition.Recognizer()
dir = os.path.dirname(os.path.abspath(sys.argv[0]))


def SpeakText(command):
    engine = pyttsx3.init()
    rate = engine.getProperty("rate")
    engine.setProperty("rate", rate-80)
    engine.say(command)
    engine.runAndWait()

def listen():
    with speech_recognition.Microphone() as source2 :
        r.adjust_for_ambient_noise(source2, duration=1)

        audio2 = r.listen(source2)

        try:
            MyText = r.recognize_google(audio2)

        except:
            SpeakText("Didn't recognise voice")
            SpeakText("Try again")
            listen()
            return
        MyText = MyText.lower()

    if MyText == "Close" or MyText == "close":
        SpeakText("Shutting down computer in 5")
        SpeakText("4")
        SpeakText("3")
        SpeakText("2")
        SpeakText("1")

        os.system('shutdown -s')

    elif MyText == "Play Song" or MyText == "play song":
        SpeakText("Playing Song E.S.M pt.2 by Snik")
        winsound.PlaySound(dir+'/SNIK - E.S.M pt.2 .wav', winsound.SND_FILENAME)

    elif MyText == "Joke" or MyText == "joke":
       SpeakText(pyjokes.get_joke())

listen()