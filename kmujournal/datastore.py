#!/usr/bin/python
# -*- coding: utf-8 -*-
from google.appengine.ext import ndb
import datetime

class Account(ndb.Model):
    search_keyword = ndb.StringProperty()
    search_keyword_record = ndb.StringProperty()
    user_searcah_date = ndb.DateTimeProperty(auto_now = True)
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

def delete_entity(User):
    User.key.delete()