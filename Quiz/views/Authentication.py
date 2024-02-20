'''
Created on Feb 6, 2024

@author: Ngo Anh Tuan
'''
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models.functions.text import Lower
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _

@login_required()
def home(request):
    context = {}
    return render(request, "home.html", context)

def sign_out(request):
    auth.logout(request)
    return redirect('quiz:sign_in')

def sign_in(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('quiz:home')
    if request.method == 'POST':
        user_password = request.POST.get('pass_word', '')
        # user_name = request.POST.get('user_name', '')
        email = request.POST.get('email', '')
        try:
            user = User.objects.annotate(email_lower=Lower('email')).get(email_lower=email.lower())
            
            user = auth.authenticate(request, username=user.username, password=user_password)
            if user is not None:
                auth.login(request, user)
                if(request.GET.get('next')):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('quiz:home')
            else:
                raise User.DoesNotExist()
        except User.DoesNotExist:
            context.update({"err":_(u"Email hoặc mật khẩu không đúng!")})
    return render(request, 'quiz/auth/sign-in.html', context)