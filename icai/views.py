import random
import requests
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.sessions import *
from icai.models import icai_registration, student_questions
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import IcaiRegistration


# Create your views here.

def home(req):
    return render(req, 'icai.html')


def home(req):
    userRegisterID = random.randint(10000, 99999)

    # if req.method == 'POST':
    #     obj = icai_registration.objects.all()
    #     obj.save()
    #     return redirect('/golive')
    # else:
    #     return render(req, 'icai.html')
    if req.method == 'POST':
        if req.POST.get('usericai_region') and req.POST.get('membershipicai_id') and req.POST.get(
                'username_icai') and req.POST.get('user_email_icai') and req.POST.get('user_contact_icai'):
            saverec = icai_registration()
            saverec.register_id = userRegisterID
            saverec.usericai_region = req.POST.get('usericai_region')
            saverec.membershipicai_id = req.POST.get('membershipicai_id')
            saverec.username_icai = req.POST.get('username_icai')
            saverec.user_email_icai = req.POST.get('user_email_icai')
            saverec.user_contact_icai = req.POST.get('user_contact_icai')
            saverec.save()
            return redirect('/golive')
            # return render(req, 'index.html')
        # else:
        #     return render(req, 'index.html')
    return render(req, 'icai.html')


def login(req):
    return render(req, 'login.html')


def over(req):
    return render(req, 'over.html')


def sessionlive(livereq):
    return render(livereq, 'webcast.html')
    # if livereq:
    #     return render(livereq, 'icai.html')
    # else:
    #     return render(livereq, 'webcast.html')


# no reload question sent by user and data will be recorded to database
def qus_send(request):
    if request.method == 'POST':
        if request.POST.get('user_question'):
            savestudentques = student_questions()
            savestudentques.qus_id  # = requests.POST('qus_id')
            savestudentques.user_question = request.POST.get('user_question')
            savestudentques.question_datetime  # = requests.POST('question_datetime')
            savestudentques.save()
            success = 'Question Sended.'
            return HttpResponse(success)
