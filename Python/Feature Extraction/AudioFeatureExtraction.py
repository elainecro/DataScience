import librosa
import sklearn
import numpy as np
import matplotlib.pyplot as plt
import librosa.display

audio_path = 'example_music.mp3'
x,sr = librosa.load(audio_path)
print(type(x),type(sr))