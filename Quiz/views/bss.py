'''
Created on Apr 4, 2024

@author: Administrator
'''
import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from scipy.io import wavfile

from QuizWebapp.settings import BASE_DIR
import matplotlib.pyplot as plt
import numpy as np


@login_required()
def source(request):
    context = {}
    # if request.method == 'POST':
    #     file =request.FILES["audio_1"]
    #     folder_path,file_name = handle_uploaded_file(file,"audio_1")
    #     standard_wav(folder_path,file_name)
    #     file =request.FILES["audio_2"]
    #     folder_path,file_name = handle_uploaded_file(file,"audio_2")
    #     standard_wav(folder_path,file_name)
    return render(request, "bss/source.html", context)

@login_required()
def source_mix(request):
    context = {}
    return render(request, "bss/source_mix.html", context)


@login_required()
def source_separation(request):
    context = {}
    return render(request, "bss/source_separation.html", context)


def handle_uploaded_file(f,file_name):
    folder_path = os.path.join(BASE_DIR, 'Quiz', 'static', 'upload')
    # strTime = datetime.now().strftime('%d%m%Y_%H%M%S')
    with open(os.path.join(folder_path,file_name+ '.wav'), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return folder_path,file_name