'''
Created on May 13, 2024

@author: NGO ANH TUAN
'''
import json
import os

import cv2
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, resolve_url

from Quiz.models.IpvSample import IpvSample
from Quiz.util import FileUtil
from QuizWebapp.settings import BASE_DIR


def image_to_text(request):
    context = {}
    try:
        samples = IpvSample.objects.all()
        context.update({'samples':samples})
    except Exception as ex:
        context.update({'has_error': str(ex)})
    return render(request, "ipv/image_to_text.html", context)


def sample(request):
    context = {}
    samples = IpvSample.objects.all()
    context.update({'samples':samples})
    return render(request, "ipv/sample.html", context)


def sample_add(request):
    context = {}
    try:
        if request.method == 'POST':
            image_name = request.POST["imgName"]
            image_file = request.FILES["image"]
            absolute_url = FileUtil.handle_uploaded_file(image_file)
            # Sample
            sample = IpvSample()
            sample.src_image_path = absolute_url
            sample.name = image_name
            sample.save()
            return redirect(resolve_url('quiz:ipv_sample'))
    except Exception as ex:
        context.update({'has_error': str(ex)})
    return render(request, "ipv/sample_add.html", context)


def sample_delete(request,sample_id):
    try:
        sample = IpvSample.objects.filter(id = sample_id)
        sample.delete()
        # check permission error
        return HttpResponse(json.dumps({'handle':'success',}), content_type="application/json");
    except Exception as ex:
        return HttpResponse(json.dumps({'handle':'error', "msg": str(ex)}), content_type="application/json")


def sample_process(request):
    try:
        sample_id = request.POST['sample_id']
        sample = IpvSample.objects.get(id = sample_id)
        src_image_path = sample.src_image_path
        folder_path = os.path.join(BASE_DIR, 'Quiz', 'static')
        file_path = os.path.join(folder_path,src_image_path)
        image = cv2.imread(file_path)
        output = process_image(image)
        print(file_path)
        return HttpResponse(json.dumps({'handle':'success','output':output}), content_type="application/json");
    except Exception as ex:
        return HttpResponse(json.dumps({'handle':'error', "msg": str(ex)}), content_type="application/json")
from pytesseract import pytesseract 
def process_image(image):
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR/tesseract.exe"
    # tessdata_dir_config = '--tessdata-dir C:\Program Files\Tesseract-OCR\tessdata'
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(image,lang='vie')
    return text.encode('utf8').decode('utf8')