'''
Created on Apr 4, 2024

@author: Administrator
'''
from _datetime import datetime
import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from scipy.io import wavfile
from scipy.signal import resample

from QuizWebapp.settings import BASE_DIR
import numpy as np


@login_required()
def source(request):
    context = {}
    if request.method == 'POST':
        file =request.FILES["audio_1"]
        handle_uploaded_file(file)
    return render(request, "bss/source.html", context)

@login_required()
def source_mix(request):
    context = {}
    return render(request, "bss/source_mix.html", context)


@login_required()
def source_separation(request):
    context = {}
    return render(request, "bss/source_separation.html", context)


def standard_wav(filename, samplerate=44100):
    # load file
    rate, data = wavfile.read(filename)
    # convert stereo to mono
    if len(data.shape) > 1:
        data = data[:, 0] / 2 + data[:, 1] / 2
    # re-interpolate sample rate    
    ratio = int(samplerate / rate)
    data = resample(data, len(data) * ratio)
    fs = samplerate
    s = data.astype(np.int16)
    folder_path = os.path.join(BASE_DIR, 'Quiz', 'static', 'upload')
    wavfile.write(folder_path + 'new_', fs, s);
    return samplerate, data.astype(np.int16)

def handle_uploaded_file(f):
    folder_path = os.path.join(BASE_DIR, 'Quiz', 'static', 'upload')
    strTime = datetime.now().strftime('%d%m%Y_%H%M%S')
    strFileName = strTime + '_' + f.name
    with open(os.path.join(folder_path,strFileName), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
