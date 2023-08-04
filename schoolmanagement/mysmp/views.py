from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Gpm
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def stud_list(request):
    gpms=Gpm.objects.all()
    return render(request,'stud_list.html',{'gpms':gpms})

@login_required
def stud_create(request):
    if request.method=='POST':
       form=TaskForm(request.POST) 
       if form.is_valid():
          form.save()
          return redirect('stud_list')
    else:
        form = TaskForm()
    return render(request,'stud_form.html',{'form':form})

@login_required
def stud_update(request, pk):
    gpml = get_object_or_404(Gpm, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=gpml)
        if form.is_valid():
            form.save()
            return redirect('stud_list')
    else:
        form = TaskForm(instance=gpml)
    return render(request, 'stud_form.html', {'form': form})

@login_required
def stud_delete(request, pk):
    gpml = get_object_or_404(Gpm, pk=pk)
    gpml.delete()
    return redirect('stud_list')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('stud_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method=='POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request,form.get_users())
            return redirect('stud_list')
    
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})   
 
def logout(request):
    auth_logout(request)
    return redirect('login')


        


