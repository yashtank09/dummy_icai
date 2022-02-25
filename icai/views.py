from django.http import Http404
from django.shortcuts import render


# Create your views here.

def home(req):
    return render(req, 'icai.html')


def login(req):
    return render(req, 'login.html')


def over(req):
    return render(req, 'over.html')


def sessionlive(req):
    return render(req, 'webcast.html')
