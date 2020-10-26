import speech_recognition as sr

reconhecedor = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        print('Diga algo...')
        audio = reconhecedor.listen(source)
        print(reconhecedor.recognize_google(audio, language='pt'))
