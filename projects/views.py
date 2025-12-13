from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from .models import projects, instruments
from .forms import create_new_instrument,create_new_projects
# Create your views here.

def view_home(request):
    return render(request,'home.html')

def view_register(request):
      if request.method=='GET':
        return render(request, 'signup.html',{
        'form':UserCreationForm
        })
      else:
        if request.POST['password1']==request.POST['password2']:
             try:
                 user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                 user.save()
                 login(request,user)
                 return redirect('projects')
             except IntegrityError:
                  return render(request, 'signup.html',{
                         'form':UserCreationForm,
                          'error':'User already exists'
                    })
             
        return render(request, 'signup.html',{
                  'form':UserCreationForm,
                  'error':'Password do not match'
                 })

def view_login(request):
   if request.method== 'GET':
        return render(request, 'login.html',{
         'form':AuthenticationForm
        })
   else:
       user=authenticate(request, username=request.POST['username'],password=request.POST['password'])
       if user is None:
            return render(request, 'login.html',{
               'form':AuthenticationForm,
               'error':'Username or password is incorrect'
            })
       else:
           login(request,user)
           return redirect('projects')

def view_logout(request):
    logout(request)
    return redirect('home')

def view_projects(request):
    project=projects.objects.all()
    return render(request,'projects.html',{
        'projects':project
    })

def view_create_project(request):
    if request.method=='GET':
        return render(request,'create_project.html',{
            'form':create_new_projects()
        })
    else:
        project=projects.objects.create(name=request.POST['name'])
        return redirect('projects')
    
def view_project_detail(request,id):
    project=get_object_or_404(projects,id=id)
    instrument=instruments.objects.filter(project_id=id)
    return render(request,'project_detail.html',{
        'project':project,
        'instruments':instrument
    })

def view_create_instrument(request,project_id):
    project=get_object_or_404(projects,id=project_id)
    if request.method=='GET':
        return render(request,'create_instrument.html',{
            'form':create_new_instrument    
        })
    else:
        instruments.objects.create(n_instrument=request.POST['n_instrument'],project=project)
        return redirect('project_detail',project_id=project.id)