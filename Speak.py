import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)

def Say(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()