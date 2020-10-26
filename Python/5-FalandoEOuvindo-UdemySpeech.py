import pyttsx3
import speech_recognition as sr
import os

fala = pyttsx3.init()
fala.say('Ei Elaine, quer ouvir um áudio?')
fala.setProperty('voice', b'brazil')
fala.setProperty('rate', 130)
fala.setProperty('volume', 1)
fala.runAndWait()

reonhecedor = sr.Recognizer()
with sr.Microphone() as source:
    print('Responda por favor...')
    audio = reonhecedor.listen(source)
    resposta = reonhecedor.recognize_google(audio, language='pt')

if resposta == 'sim':
    fala.say('Ok, executando o áudio')
    fala.setProperty('voice', b'brazil')
    fala.setProperty('rate', 130)
    fala.setProperty('volume', 1)
    fala.runAndWait()

    os.system('GoodMorningSunshine.wav')

elif resposta == 'não':
    fala.say('Então vamos encerrando o programa. Tchau, beijos!')
    fala.setProperty('voice', b'brazil')
    fala.setProperty('rate', 130)
    fala.setProperty('volume', 1)
    fala.runAndWait()