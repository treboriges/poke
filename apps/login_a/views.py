# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from models import User
def index(request):
    # User.objects.all().delete()
    return render(request, 'login_a/index.html')

def register(request):
    results = User.objects.validate(request.POST)
    if results['status'] == True:
        user = User.objects.creator(request.POST)
        messages.success(request, "User has been created")
    else:
        for error in results['errors']:
            messages.error(request, error)
    return redirect('/')
def login(request):
    results = User.objects.loginVal(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['name'] = results['users'].name
        request.session['email']= results['users'].email
        request.session['userid'] = results['users'].id
        return redirect('/dashboard/')


def logout(request):
    request.session.flush()
    return redirect('/')
