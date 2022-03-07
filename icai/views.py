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
    if req.method == 'POST':
        # objects for fetching data from input fields using their `name` attributes
        UserRegion = req.POST['usericai_region']
        MembershipID = req.POST['membershipicai_id']
        UserName = req.POST['username_icai']
        UserEmailID = req.POST['user_email_icai']
        UserContactNo = req.POST['user_contact_icai']

        # if all objects will get values then save data to our database
        if UserRegion and MembershipID and UserName and UserEmailID and UserContactNo:
            # This is database object
            RegiDataSave = icai_registration()

            # Add database object values to database
            RegiDataSave.register_id = userRegisterID
            RegiDataSave.usericai_region = UserRegion
            RegiDataSave.membershipicai_id = MembershipID
            RegiDataSave.username_icai = UserName
            RegiDataSave.user_email_icai = UserEmailID
            RegiDataSave.user_contact_icai = UserContactNo
            # Save data to Database
            RegiDataSave.save()

            # after successfully data saved it redirects to below page
            return redirect('/golive')
    else:
        # if request method dose not match it will return 'icai.html'/ Same Page
        return render(req, 'icai.html')


def sessionlive(livereq):
    icai_registration.objects.get(register_id=livereq.session['userid'], username_icai=livereq.session['username'])
    if livereq.session.has_key('userid'):
        print(livereq.session.get('userid'))
        print(livereq.session.get('username'))
        return render(livereq, 'webcast.html')
    else:
        return render(livereq, 'icai.html')


def login(req):
    return render(req, 'login.html')


def over(req):
    return render(req, 'over.html')


# no reload question sent by user and data will be recorded to database
def qus_send(request):
    if request.method == 'POST':
        if request.POST.get('user_question'):
            savestudentques = student_questions()
            savestudentques.qus_id
            savestudentques.username = request.session.get('username')
            savestudentques.user_question = request.POST.get('user_question')
            savestudentques.question_datetime
            savestudentques.UserRegID = request.session.get('userid')
            savestudentques.save()
            success = 'Question Sended.'
            return HttpResponse(success)