from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm

def home(req):
    # return HttpResponse("hello")
    return render(req, 'pages/home.html')
    

def about(req):
    return render(req, 'pages/about.html')

def apply(req):
    context = {}
    if req.method is 'POST' :
        pass

    context['form'] = StudentForm()
    return render(req, 'pages/apply.html',context)
