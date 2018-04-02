#!/usr/bin/python
# -*- coding: utf-8 -*-
from kmujournal.message import return_message, return_keyboard,update_message, remove_keyboard
from kmujournal.crawlr_hpg import get_contents
from kmujournal.crawlr_fac import get_flash
from kmujournal.datastore import create_entity_using_keyword_arguments, save_entity, get_entity, delete_entity
import datetime

def first_process():
    code = 200
    kyb =return_keyboard()
    return kyb, code

def af_clk_procees(data):
    code = 200

    user_key = data.json["user_key"]
    #request_type = data.json["type"]
    content = data.json["content"]

    if get_entity(user_key) == None:
        user=create_entity_using_keyword_arguments(user_key)
        save_entity(user)
    user=get_entity(user_key)
    user.search_keyword_record = str(user.search_keyword_record)+str(content) +'&'+str(datetime.datetime.now())+'\n'
    save_entity(user)

    if content == u'최신 기사':
        msg = return_message()
        return update_message(msg, get_contents()), code

    elif content == u'단신 & 속보':
        msg = return_message()
        return update_message(msg, get_flash()), code

    elif content == u'제보 방법':
        msg = return_message()
        report =get_entity("admin_User")
        udt_msg =update_message(msg, report.search_keyword+
                                    u"\n============================\n"
                                    u"키보드 1시 방향의 [1:1]를 누르세요\n"
                                     u"on/off로 대화가 가능합니다.\n"
                                )
        return udt_msg, code
    else:
        msg = return_message()
        return msg, code

def update_report(data):
    report =get_entity("admin_User")
    content = data.json["content"]

    report.search_keyword= content
    save_entity(report)
    msg = return_message()
    msg = update_message(msg,content)
    return msg, 200

def add_friend(data):
    User = create_entity_using_keyword_arguments(data.json["user_key"])
    save_entity(User)
    return 200

def delete_friend(user_key):
    User=get_entity(user_key)
    delete_entity(User)
    return 200

def exit_friend(user_key):
    User=get_entity(user_key)
    User.switch = False
    save_entity(User)
    return 200