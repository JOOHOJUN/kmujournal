#!/usr/bin/python
# -*- coding: utf-8 -*-
from kmujournal.message import return_message, return_keyboard,update_message, remove_keyboard
from kmujournal.crawlr_hpg import get_contents
from kmujournal.crawlr_fac import get_flash
import re

def first_process():
    code = 200
    return return_keyboard(), 200

def af_clk_procees(data):
    code = 200

    user_key = data.json["user_key"]
    #request_type = data.json["type"]
    content = data.json["content"]

    if content == u'최신 기사':
        msg = return_message()
        return update_message(msg, get_contents()), code

    elif content == u'단신 & 속보':
        msg = return_message()
        return update_message(msg, get_flash()), code

    elif content == u'제보 방법':
        msg = return_message()
        udt_msg =update_message(msg, u"익명 보장합니다.\n"
                                     u"키보드 1시 방향의 [1:1]를 누르세요\n"
                                     u"on/off로 대화가 가능합니다.")
        '''메시지에 그림 있다면'''
        return udt_msg, 200
    else:
        msg = return_message()
        return msg, 200

def add_friend(data):
    return 200

def delete_friend(user_key):
    return 200