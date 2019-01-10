from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

#from lab7.models import Bullet
from lab7.forms import *
from lab7.models import *
from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,logout
from django.contrib import auth

# Create your views here.

class ExampleView(View):
    def get(self, request):
        return render(request, 'base.html')

class BulletsView(ListView):
    model = Bullet
    context_object_name = 'bullets'
    template_name = 'bullets.html'
    
    def get_queryset(self):
        qs = Bullet.objects.all().order_by('id').values()
        return qs

class BulletView(View):
    def get(self, request, id):
        data = Bullet.objects.get(id__exact=id)
        return render(request, 'bullet.html', {'bullet':data})

def registration_old(request):
    errors = []
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors.append('Login required')
        elif len(username)<5:
            errors.append('Login should be 5 or more symbols')
        
        password = request.POST.get('password')
        if not password:
            errors.append('Password required')
        elif len(password)<6:
            errors.append('Password length should be 6 or more')
        
        password_repeat = request.POST.get('password2')
        
        if password != password_repeat:
            errors.append('Password should be similar')
        
        if not errors:
            
            return HttpResponseRedirect('/lab7/login')
    return render(request, 'lab7/logon.html', {'errors': errors})

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/lab7/')
        return render(request, 'signup.html', {'form': form})
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})

def authorization(request):
    redirect_url = '/lab7/'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['login'],
                                     password=form.cleaned_data['password'])
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect(redirect_url)
            else:
                form.add_error(None, 'Wrong login or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form, 'continue': redirect_url})

@login_required
def exit(request):
    logout(request)
    return render(request, 'logout.html')
