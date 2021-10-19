import speech_recognition as sr

def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source, 0, 4)

    try:
        print("Recognizing....")
        query = str(r.recognize_google(audio, language='en-in'))
        print(f"You Said: {query}")

    except:
        print("Say that again please....")
        return ""

    return query.lower()

def ListenHindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source, 0, 4)

    try:
        print("Recognizing....")
        query = str(r.recognize_google(audio, language='hi'))
        print(f"You Said: {query}")

    except:
        print("Say that again please....")
        return ""

    return query.lower()