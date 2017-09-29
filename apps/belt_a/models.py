# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_a.models import User
class Poke(models.Model):
    giver = models.ForeignKey(User, related_name = 'gave')
    receiver = models.ForeignKey(User, related_name='received')
