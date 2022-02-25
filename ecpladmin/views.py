from django.shortcuts import render


# Create your views here.


def admin(req):
    return render(req, 'index.html')


def dashboard(req):
    return render(req, 'dashboard.html')
