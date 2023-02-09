from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import StudentForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as handleLogin , authenticate

def home(req):
    # return HttpResponse("hello")
    return render(req, 'pages/home.html')
    

def login(req):
    form = AuthenticationForm(req , req.POST or None)
    if req.method == 'POST':
        if(form.is_valid()):
            user = authenticate(request=req , username = req.POST['username'] , password = req.POST['password'])
            if(user != None):
                handleLogin(req, user)
                print("in iffffffffffffffffffffffffff")
                return redirect("home")
            else:
                print("wrong")
    return render(req, 'pages/login.html',{"form":form})

def apply(req):
    try:
        context = {}
        form = StudentForm(req.POST or None , req.FILES or None)
        if req.method == 'POST' :
            if form.is_valid():
                form.save()
                redirect('apply')
            else :
                raise Exception("Someting Went wrong")
        context['form'] = StudentForm()
        return render(req, 'pages/apply.html',context)
    except Exception as e:
        return render(req, 'pages/apply.html',context)

