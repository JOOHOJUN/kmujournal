#!/usr/bin/python
# -*- coding: utf-8 -*-
def return_keyboard():
    home_buttons = [
        u"최신 기사",
        u"최신 속보",
        u"제보 하기",
    ]

    _base_keyboard = {
        "type": "buttons",
        "buttons": home_buttons,
    }
    return _base_keyboard

def return_message():

    _base_message = {
        "message": {
            "text": "TEXT_MESSAGE",
        },
        "keyboard": return_keyboard(),
    }

    return _base_message

def update_message(msg, message):
    msg['message']['text'] = message
    return msg

def remove_keyboard(msg):
    msg['keyboard'] = ''
    return msg

