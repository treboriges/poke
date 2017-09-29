# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login_a.models import User
from models import Poke
def index(request):
    context = {
        'other_users': User.objects.exclude(id = request.session['userid']),
        'current_user': User.objects.get(id = request.session['userid']),
        'pokedme': [],
        'pokecount': [],
        }
    ids = context['current_user'].received.all().values('giver__id').distinct()
    for bleh in ids:
        context['pokedme'].append(User.objects.get(id=bleh['giver__id']))
        # context['pokecount'] += 1
    # receiveids = context['other_users'].gave.all().values('receiver__id').distinct()
    # for user in other_users:
    # others = User.objects.get(id = otherid)
    # for user in others:
    #     if ids:
    #         context['pokecount'] += 1
    # liketracker = context['current_user'].received.all()
    # print liketracker.count()
    for user in context['other_users']:
        context['pokecount'] = user.gave.all().count()
        # for i in context['pokecount']:
        #     pass


    return render(request, 'belt_a/dashboard.html', context)

def poke(request, otherid):
    current = User.objects.get(id = request.session['userid'])
    others = User.objects.get(id = otherid)
    Poke.objects.create(giver = current, receiver = others)
    return redirect('/dashboard/')
