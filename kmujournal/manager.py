#!/usr/bin/python
# -*- coding: utf-8 -*-
from kmujournal.message import return_message, update_message, remove_keyboard
from kmujournal.crawlr_hpg import get_contents
import re
from kmujournal.dbman import return_status, change_status, add_user, delete_user

def first_process():
    code = 200
    return return_message(), 200

def af_clk_procees(data):
    code = 200

    user_key = data.json["user_key"]
    #request_type = data.json["type"]
    content = data.json["content"]

    if return_status(user_key):
        if content == u'최신 기사':
            msg = return_message()
            return update_message(msg, get_contents()), code

        elif content == u'최신 속보':
            msg = return_message()
            return update_message(msg, u'text'), code

        elif content == u'제보 하기':
            msg = return_message()
            udt_msg =update_message(msg, u"제보할 내용을 쓰세요."
                                        u"끝내려면 끝에다 '제보끝'이라고 쓰세요."
                                        u"---------------------------"
                                        u"제보 받고 있습니다.")
            '''메시지에 그림 있다면'''
            udt_msg = remove_keyboard(udt_msg)
            change_status(user_key)
            return udt_msg, 200
    else:
        if re.search(u'제보끝', content) !=None:
            change_status(user_key)
            return return_message(), 200
        else:
            msg = return_message()
            msg = update_message(msg, u"끝내려면 끝에다 '제보끝'이라고 쓰세요.")
            msg = remove_keyboard(msg)
            return msg, 200

def add_friend(data):
    key = data.json['user_key']
    add_user(key)
    return 200

def delete_friend(user_key):

    if delete_user(user_key) == 0:
        return 200
    else:
        return 100