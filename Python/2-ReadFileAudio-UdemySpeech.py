import speech_recognition as sr

reconhecedor = sr.Recognizer()

caminhosAudios = ['HelloHowAreYou.wav', 'HelloThisIsATest.wav', 'GoodMorningSunshine.wav']

for caminho in caminhosAudios:
    print(caminho)

    with sr.AudioFile(caminho) as source:
        audio = reconhecedor.record(source)
        print(reconhecedor.recognize_sphinx(audio))