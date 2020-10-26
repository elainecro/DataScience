import speech_recognition as sr

reconhecedor = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        reconhecedor.adjust_for_ambient_noise(source, duration=3)
        print('Diga algo')
        audio = reconhecedor.listen(source)
        print(reconhecedor.recognize_sphinx(audio))
