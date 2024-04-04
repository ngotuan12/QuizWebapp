'''
Created on Apr 4, 2024

@author: Administrator
'''
import os
from pathlib import Path

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from scipy.io import wavfile
from scipy.signal import resample

from QuizWebapp.settings import BASE_DIR
import matplotlib.pyplot as plt
import numpy as np


@login_required()
def source(request):
    context = {}
    if request.method == 'POST':
        file =request.FILES["audio_1"]
        folder_path,file_name = handle_uploaded_file(file,"audio_1")
        standard_wav(folder_path,file_name)
        file =request.FILES["audio_2"]
        folder_path,file_name = handle_uploaded_file(file,"audio_2")
        standard_wav(folder_path,file_name)
    return render(request, "bss/source.html", context)

@login_required()
def source_mix(request):
    context = {}
    return render(request, "bss/source_mix.html", context)


@login_required()
def source_separation(request):
    context = {}
    return render(request, "bss/source_separation.html", context)

def standard_wav(folder_path,filename, samplerate=48000):
    # load file
    rate, data = wavfile.read(os.path.join(folder_path,filename+ '.wav'))
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
    wavfile.write(os.path.join(folder_path,new_file_name+ '.wav' ), fs, s);
    img_file_name = 'signal_' + filename
    img_path = os.path.join(folder_path,img_file_name+ '.png')
    os.remove(img_path) if os.path.exists(img_path) else None
    plt.plot(s)
    plt.savefig(os.path.join(folder_path,img_file_name))
    plt.close()
    return samplerate, data.astype(np.int16)
def handle_uploaded_file(f,file_name):
    folder_path = os.path.join(BASE_DIR, 'Quiz', 'static', 'upload')
    # strTime = datetime.now().strftime('%d%m%Y_%H%M%S')
    with open(os.path.join(folder_path,file_name+ '.wav'), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return folder_path,file_name