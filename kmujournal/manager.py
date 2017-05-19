#!/usr/bin/python
# -*- coding: utf-8 -*-
from kmujournal.message import return_message, return_keyboard,update_message, remove_keyboard
from kmujournal.crawlr_hpg import get_contents
from kmujournal.crawlr_fac import get_flash
from kmujournal.datastore import create_entity_using_keyword_arguments, save_entity, get_entity

def first_process():
    code = 200
    kyb =return_keyboard()
    return kyb, code

def save_userkey(data):
    User =create_entity_using_keyword_arguments(data.json["user_key"])
    save_entity(User)
    user1=get_entity(data.json["user_key"])

    msg = return_message()
    msg =update_message(msg, user1.user_key)
    return msg, 200

def af_clk_procees(data):
    code = 200

    user_key = data.json["user_key"]
    #request_type = data.json["type"]
    content = data.json["content"]

    msg = return_message()
    user1 = get_entity(data.json["user_key"])
    return update_message(msg, user1.user_key), code

    if content == u'최신 기사':
        msg = return_message()
        return update_message(msg, get_contents()), code

    elif content == u'단신 & 속보':
        msg = return_message()
        return update_message(msg, get_flash()), code

    elif content == u'제보 방법':
        msg = return_message()
        udt_msg =update_message(msg, u"키보드 1시 방향의 [1:1]를 누르세요\n"
                                     u"on/off로 대화가 가능합니다.\n"
                                     u"============================\n"
                                     u"교강사의 부적절한 발언을\n"
                                     u"제보받고 있습니다.\n"
                                     u"ex)성차별적, 성소수자 혐오발언 등")
        '''메시지에 그림 있다면'''
        return udt_msg, code
    else:
        msg = return_message()
        return msg, code

def add_friend(data):
    return 200

def delete_friend(user_key):
    return 200