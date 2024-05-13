'''
Created on May 13, 2024

@author: NGO ANH TUAN
'''
import os

from QuizWebapp.settings import BASE_DIR
from datetime import datetime

def handle_uploaded_file( file):
    folder_path = os.path.join(BASE_DIR, 'Quiz', 'static', 'upload','ipv')
    strTime = datetime.now().strftime('%d%m%Y_%H%M%S')
    file_name, file_extension = os.path.splitext(file.name)
    file_name = file_name + '_'+ strTime
    if os.path.isdir(folder_path) == False:
        os.makedirs(folder_path)
    absolute_url = 'upload' +'/ipv/' + file_name +file_extension
    with open( os.path.join(folder_path,file_name+file_extension), 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return absolute_url