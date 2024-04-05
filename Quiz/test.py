'''
Created on Feb 6, 2024

@author: Ngo Anh Tuan
'''
from _datetime import datetime
import os

from scipy.io import wavfile
from scipy.signal import resample

from QuizWebapp.settings import BASE_DIR
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
# import pylab as pl
def load_wav(filename, samplerate=44100):
    # load file
    rate, data = wavfile.read(filename)

    # convert stereo to mono
    if len(data.shape) > 1:
        data = data[:, 0] / 2 + data[:, 1] / 2

    # re-interpolate samplerate    
    ratio = int(samplerate / rate)
    data = resample(data, len(data) * ratio)

    return samplerate, data.astype(np.int16)


def handle_uploaded_file(f):
    folder_path = os.path.join(BASE_DIR, 'Quiz', 'static', 'upload')
    strTime = datetime.now().strftime('%d%m%Y_%H%M%S')
    if os.path.isdir(folder_path) == False:
        os.makedirs(folder_path)
    with open(folder_path + strTime + '_' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def mix_source():
    fs1, s1 = load_wav('D:\\projects\\mse\\QuizWebapp\\Quiz\\static\\upload\\audio_1.wav')
    fs2, s2 = load_wav('D:\\projects\\mse\\QuizWebapp\\Quiz\\static\\upload\\audio_2.wav')
    length = max([len(s1), len(s2)])
    s1.resize((length, 1), refcheck=False)
    s2.resize((length, 1), refcheck=False)
    """
    The function numpy.c_ concatenates the numpy arrays given as input.
    The method numpy_array.T is the transpose operation that allow us
    to prepare an input source matrix of the right size (3, length),
    according to the chosen mixing matrix (3,3).
    """
    S = (np.c_[s1, s2]).T
    # Mixing Matrix
    # A = np.random.uniform(size=(2,2))
    A = np.array([[1, 0.5],
              [0.5, 1],
              ])
    print ('Mixing Matrix:')
    print (A.round(2))
    # Mixed Signals
    X = np.dot(A, S)
    for i in range(X.shape[0]):
        sn = (X[i]).astype(np.int16)
        plt.plot(sn)
        plt.show()
        wavfile.write("D:/%i_audio_mix.wav"%i, fs1, sn)
if __name__ == '__main__':
    mix_source()
    fs3, s3 = load_wav('audio3.wav')  # Protoss Zealot - "My life for Aiur!"
    wavfile.write("D:/new_audio_3.wav", fs3, s3);
    # plot
    # pl.figure(figsize=(6.75,2))
    # pl.plot(s3)
    # pl.title('Signal 3')
    # pl.show()
    # pl.show()
    plt.plot(s3)
    plt.savefig('D:/foo.png')
    # plt.show()
