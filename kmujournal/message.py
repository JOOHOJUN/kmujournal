#!/usr/bin/python
# -*- coding: utf-8 -*-
def return_keyboard():
    home_buttons = [
        u"최신 기사",
        u"단신 & 속보",
        u"제보 방법",
    ]

    _base_keyboard = {
        "type": "buttons",
        "buttons": home_buttons,
    }
    return _base_keyboard

def return_message():

    _base_message = {
        "message": {
            "text": "어서오세요",
        },
        "keyboard": return_keyboard(),
    }

    return _base_message

def update_message(msg, message):
    msg['message']['text'] = message
    return msg

def remove_keyboard(msg):
    del msg['keyboard']
    return msg

