import speech_recognition as sr
import pyaudio

def SpeechToText():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except:
        return ""


def StringEval(word):
    #Plus
    word = word.replace("plus", "+")
    word = word.replace("add", "+")
    #Minus
    word = word.replace("minus", "-")
    word = word.replace("subtract", "-")
    word = word.replace("take away", "-")
    #Multiply
    word = word.replace("multiply", "*")
    word = word.replace("times", "*")
    word = word.replace("x", "*")
    #Divide
    word = word.replace("divide by", "/")
    word = word.replace("over", "/")
    word = word.replace("divide", "/")
    #back-up
    word = word.replace(",", "")
    word = word.replace(" ", "")    
    try:
        return str(eval(word))
    except:
        return "error"
