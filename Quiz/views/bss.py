'''
Created on Apr 4, 2024

@author: Administrator
'''
import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import matplotlib
from scipy.io import wavfile
from scipy.signal import resample

from QuizWebapp.settings import BASE_DIR
import matplotlib.pyplot as plt
import numpy as np


@login_required()
def source(request):
    context = {}
    if request.method == 'POST':
        file = request.FILES["audio_1"]
        folder_path, file_name = handle_uploaded_file(file, "audio_1")
        standard_wav(folder_path, file_name)
        file = request.FILES["audio_2"]
        folder_path, file_name = handle_uploaded_file(file, "audio_2")
        standard_wav(folder_path, file_name)
    return render(request, "bss/source.html", context)


@login_required()
def source_mix(request):
    context = {}
    if request.method == 'POST':
        mix_source()
    return render(request, "bss/source_mix.html", context)


@login_required()
def source_separation(request):
    context = {}
    if request.method == 'POST':
        separation()
    return render(request, "bss/source_separation.html", context)


def standard_wav(folder_path, filename, samplerate=48000):
    matplotlib.use('agg')
    # load file
    rate, data = wavfile.read(os.path.join(folder_path, filename + '.wav'))
    plt.plot(data)
    plt.savefig(os.path.join(folder_path,'signal_real_' +filename+'.png'))
    plt.close()
    # convert stereo to mono
    if len(data.shape) > 1:
        data = data[:, 0] / 2 + data[:, 1] / 2
    # re-interpolate sample rate    
    ratio = int(samplerate / rate)
    data = resample(data, len(data) * ratio)
    fs = samplerate
    s = data.astype(np.int16)
    folder_path = os.path.join(BASE_DIR, 'Quiz', 'static', 'upload')
    new_file_name = 'new_' + filename
    wavfile.write(os.path.join(folder_path, new_file_name + '.wav'), fs, s);
    img_file_name = 'signal_' + filename
    img_path = os.path.join(folder_path, img_file_name + '.png')
    os.remove(img_path) if os.path.exists(img_path) else None
    plt.plot(s)
    plt.savefig(os.path.join(folder_path, img_file_name))
    plt.close()
    return samplerate, data.astype(np.int16)


def handle_uploaded_file(f, file_name):
    folder_path = os.path.join(BASE_DIR, 'Quiz', 'static', 'upload')
    # strTime = datetime.now().strftime('%d%m%Y_%H%M%S')
    with open(os.path.join(folder_path, file_name + '.wav'), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return folder_path, file_name


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


def mix_source():
    matplotlib.use('agg')
    folder_path = os.path.join(BASE_DIR, 'Quiz', 'static', 'upload')
    file_name_1 = 'audio_1'
    file_name_2 = 'audio_2'
    full_path_1 = os.path.join(folder_path, file_name_1 + '.wav')
    full_path_2 = os.path.join(folder_path, file_name_2 + '.wav')
    fs1, s1 = load_wav(full_path_1)
    fs2, s2 = load_wav(full_path_2)
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
        file_name_i = 'audio_mix_%i.wav' % (i + 1)
        img_file_name = 'mix_signal_%i.png' % (i + 1)
        full_path_i = os.path.join(folder_path, file_name_i)
        img_path = os.path.join(folder_path, img_file_name)
        os.remove(img_path) if os.path.exists(img_path) else None
        sn = (X[i]).astype(np.int16)
        plt.plot(sn)
        plt.savefig(img_path)
        plt.close()
        wavfile.write(full_path_i, fs1, sn)
import shutil
def separation():
    folder_path = os.path.join(BASE_DIR, 'Quiz', 'static', 'upload')
    file_name_1 = 'audio_1'
    separation_audio_1 = 'separation_audio_1'
    separation_path_1 = os.path.join(folder_path, separation_audio_1 + '.wav')
    os.remove(separation_path_1) if os.path.exists(separation_path_1) else None
    shutil.copyfile(os.path.join(folder_path, file_name_1 + '.wav'), separation_path_1)
    folder_path = os.path.join(BASE_DIR, 'Quiz', 'static', 'upload')
    #
    file_name_1 = 'audio_2'
    separation_audio_1 = 'separation_audio_2'
    separation_path_1 = os.path.join(folder_path, separation_audio_1 + '.wav')
    os.remove(separation_path_1) if os.path.exists(separation_path_1) else None
    shutil.copyfile(os.path.join(folder_path, file_name_1 + '.wav'), separation_path_1)
    #
    file_name_1 = 'signal_real_audio_1'
    separation_audio_1 = 'separation_signal_1'
    separation_path_1 = os.path.join(folder_path, separation_audio_1 + '.png')
    os.remove(separation_path_1) if os.path.exists(separation_path_1) else None
    shutil.copyfile(os.path.join(folder_path, file_name_1 + '.png'), separation_path_1)
    #
    file_name_1 = 'signal_real_audio_2'
    separation_audio_1 = 'separation_signal_2'
    separation_path_1 = os.path.join(folder_path, separation_audio_1 + '.png')
    os.remove(separation_path_1) if os.path.exists(separation_path_1) else None
    shutil.copyfile(os.path.join(folder_path, file_name_1 + '.png'), separation_path_1)