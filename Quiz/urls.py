'''
Created on Feb 6, 2024

@author: Ngo Anh Tuan
'''

from django.urls.conf import path
from Quiz.views import Authentication as auth_views
from Quiz.views import Question as question_views
from Quiz.views import Subject as subject_views
from Quiz.views import Exam as exam_views

from Quiz.views import Practice as practice_views
from Quiz.views import History as history_views
from Quiz.views import Certificate as certificate_views

app_name = 'quiz'

urlpatterns = [
    path('', auth_views.home , name='home'),
    path('question/', question_views.index , name='question'),
    # subject
    path('subject/', subject_views.index , name='subject'),
    path('subject/add/', subject_views.add , name='subject_add'),
    path('subject/edit/<int:subject_id>/', subject_views.edit , name='subject_edit'),
    path('subject/delete/<str:subject_id>/', subject_views.delete , name='subject_delete'),
    # exam
    path('exam/', exam_views.index , name='exam'),
    path('practice/', practice_views.index , name='practice'),
    path('history/', history_views.index , name='history'),
    path('certificate/', certificate_views.index , name='certificate'),
    path('sign/out/', auth_views.sign_out , name='sign_out'),
    path('sign/in/', auth_views.sign_in , name='sign_in'),
    ]
