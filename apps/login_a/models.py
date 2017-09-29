# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def loginVal(self, postData):
        results = {
            'status': True,
            'errors': [],
            'users': None
        }
        user = User.objects.filter(email = postData['email'])
        if len(user) < 1:
            results['errors'].append("Your name and/or password is invalid")
            results['status'] = False
        else:
            results['users'] = user[0]
        return results
    def creator(self, postData):
        user = self.create(name = postData['name'],alias = postData['alias'], email = postData['email'],password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()), dob = postData['dob'])
        return user
    def validate(self, postData):
        results = {
            'status': True,
            'errors': []
        }
        if len(postData['name']) < 3:
            results['status'] = False
            results['errors'].append("Name needs to be more than 3 characters")
        if len(postData['alias']) < 3:
            results['status'] = False
            results['errors'].append("Alias needs to be more than 3 characters")
        if len(postData['email']) < 3:
            results['status'] = False
            results['errors'].append("Email needs to be more than 3 characters")
        if not re.match('[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]', postData['email']):
            results['status'] = False
            results['errors'].append("Email is not valid")
        if len(postData['password']) < 5:
            results['status'] = False
            results['errors'].append("email is too short")
        if postData['password'] != postData['c_password']:
            results['status'] = False
            results['errors'].append("Passwords do not match!")
        # if postData['dob'] == None:
        #     results['status'] = False
        #     results['errors'].append("Please enter a valid date"
        if postData['name'].strip ('') < 1:
            results['status'] = False
            results['errors'].append("Uh, that's not a name")
        return results
class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    dob = models.DateField()
    count = models.IntegerField(default = 0)
    objects = UserManager()
