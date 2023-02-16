from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as handleLogin , authenticate , logout as handleLogout
from django.contrib.auth.decorators import login_required

@login_required()
def home(req):
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

@login_required()
def apply(req):
    try:
        context = {}
        form = StudentForm(req.POST or None , req.FILES or None)
        if req.method == 'POST' :
            if form.is_valid():
                form.save()
                return redirect('apply')
            else :
                raise Exception("Someting Went wrong")
        context['form'] = StudentForm()
        return render(req, 'pages/apply.html',context)
    except Exception as e:
        return render(req, 'pages/apply.html',context)

def logout(req):
    handleLogout(req)
    return redirect("login")

@login_required()
def applied_students(req):
    context = {}
    if(req.GET.get('is_approved')=='true'):
        context['students'] = Student.objects.filter(is_approved=True)
    else :
        context['students'] = Student.objects.filter(is_approved=False)
    return render(req, 'pages/applied_students.html',context)

@login_required()
def student_details(req,id):
    context = {}
    context['student'] = Student.objects.get(pk=id)
    return render(req, 'pages/student_details.html',context)

@login_required()
def approve(req,id):
    student = Student.objects.get(pk=id)
    student.is_approved = True
    student.save()
    return redirect(req.META.get('HTTP_REFERER'))

@login_required()
def edit(req,id):
    try:
        student = Student.objects.get(pk=id)
        if req.method == 'POST':
            form = StudentForm(req.POST or None , req.FILES or None , instance=student)
            if req.method == 'POST' :
                if form.is_valid():
                    form.save()
                    return redirect('applied_students')
                else :
                    raise Exception("Someting Went wrong")
        else:
            form = StudentForm(instance=student)
            context = {'form':form}
            return render(req, 'pages/edit.html',context)   
    except Exception as e:
        return render(req, 'pages/edit.html',context)   

@login_required()
def delete(req,id):
    try:
        student = Student.objects.get(pk=id).delete()
        return redirect("applied_students")
    except Exception as e:
        return render(req, 'pages/edit.html',context)   
