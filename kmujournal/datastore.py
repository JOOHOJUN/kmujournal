#!/usr/bin/python
# -*- coding: utf-8 -*-
from google.appengine.ext import ndb
import datetime

class Account(ndb.Model):
    user_key = ndb.StringProperty()
    user_searcah_date = ndb.DateProperty(auto_now_add = True)
    switch = ndb.BooleanProperty()                             #제보하기 스위치

def create_entity_using_keyword_arguments(user_key):
    User = Account(
        user_searcah_date=datetime.datetime.now(), switch=True, id=user_key)   #id로 검색
    return User

def save_entity(User):
    User.put()

def get_entity(user_key):
    User_key = ndb.Key(Account, user_key)
    User = User_key.get()
    return User