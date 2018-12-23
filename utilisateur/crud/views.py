# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Utilisateur
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponse,HttpRequest
import re

##########
from django.views.generic import UpdateView
from django.template.loader import render_to_string
# Create your views here.

class UtilisateursForm(ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['id', 'nom', 'pre', 'email', 'login', 'psw']


def index(HttpRequest):
    if HttpRequest.GET:
        #print HttpRequest.GET
        log= HttpRequest.GET['login']
        if log == 'login':
            username = HttpRequest.GET['username']
            password = HttpRequest.GET['password']
           # inscription = HttpRequest.GET['inscription']

            return utilisateur_check_login(HttpRequest,username,password)
        else:
            #return render(HttpRequest,template_name='crud/inscription.html')
            return redirect('http://127.0.0.1:8000/crud/inscription/')
    else:
        return render(HttpRequest, template_name='crud/utilisateur_list.html')


def login(request):
    print HttpRequest.GET


def disconnect(HttpRequest):
    print HttpRequest.GET
    if HttpRequest.GET:
        disc=HttpRequest.GET['disconnect']
        if disc =='disconnect':
            return redirect('http://127.0.0.1:8000/crud/index/')


def utilisateur_check_login(HttpRequest,username,password):
    utilisateur = Utilisateur.objects.filter(login=username,psw=password)
    username = HttpRequest.GET['username']
    password = HttpRequest.GET['password']
    if utilisateur:
        return redirect('http://127.0.0.1:8000/crud/details/'+username+'/'+password+'/')
    else:
        return redirect('http://127.0.0.1:8000/crud/index/')


def utilisateur_details( HttpRequest,template_name='crud/dash.html'):
    if not HttpRequest.GET:
        url=  HttpRequest.get_full_path()
        username = re.search('\/[a-z]*\/[a-z]*\/(.+?)\/[a-z0-9]*', url)
        username = username.group(1)
        password = re.search('\/[a-z]*\/[a-z]*\/[]a-z0-9]*\/(.+?)\/', url)
        password = password.group(1)

        utilisateur = Utilisateur.objects.filter(login=username, psw=password)
        #return render(request,template_name)
        data = {}
        data['object_list'] = utilisateur
        return render(HttpRequest, template_name, data)
    else:
        print HttpRequest.GET['disconnect']
        if HttpRequest.GET['disconnect'] == 'disconnect':
            return redirect('http://127.0.0.1:8000/crud/index/')
        else:
            email = HttpRequest.GET['email']
            username = HttpRequest.GET['username']
            password = HttpRequest.GET['password']
            Utilisateur.objects.filter(login=username,psw=password).values().update(email=email)
            print Utilisateur.objects.filter(login=username,psw=password).values()


            return redirect('http://127.0.0.1:8000/crud/details/'+username+'/'+password+'/')

def utilisateur_update(HttpRequest):
    return render(HttpRequest,template_name='crud/update.html')



def utilisateur_not_found(request):
    return render(request,template_name='crud/404.html')



def inscription(HttpRequest):
    if HttpRequest.GET:
        print HttpRequest.GET
        log = HttpRequest.GET['login']
        if log == 'inscription':
            username = HttpRequest.GET['username']
            password = HttpRequest.GET['password']
            first_name = HttpRequest.GET['first_name']
            last_name = HttpRequest.GET['last_name']
            password_confirmation = HttpRequest.GET['password_confirmation']
            email = HttpRequest.GET['email']
            # inscription = HttpRequest.GET['inscription']
            if password == password_confirmation :
                return check_db(username,password,first_name,last_name,email)
            else:
                return redirect('http://127.0.0.1:8000/crud/inscription/')

        else:
            # return render(HttpRequest,template_name='crud/inscription.html')
            return redirect('http://127.0.0.1:8000/crud/index/')
    else:
        return render(HttpRequest, template_name='crud/inscription.html')


def check_db(username,password,first_name,last_name,email):
    utilisateur = Utilisateur.objects.filter(login=username)
    if utilisateur:
        return redirect('http://127.0.0.1:8000/crud/inscription/')
    else:
        utilisateur = Utilisateur(email=email,psw=password,pre=first_name,nom=last_name,login=username)
        utilisateur.save()
        return redirect('http://127.0.0.1:8000/crud/index/')

