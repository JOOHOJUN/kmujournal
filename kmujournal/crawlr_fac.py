#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import re
from bs4 import BeautifulSoup


def get_items():
    One_url = 'http://www.kookminjournal.com/rss'
    res = urllib2.urlopen(One_url)
    data = res.read()
    soup = BeautifulSoup(data, 'html.parser')
    items = soup.find_all('item')

    return items

def get_url(get_items):
    url_list = []
    r = re.compile(u'단신&속보')
    for i in get_items:
        if r.search(i.find('category').text) != None :
            url_list.append(i.find('guid').text)

    return url_list

def get_titles(get_items):
    titles_list = []
    r = re.compile(u'단신&속보')
    for i in get_items:
        if r.search(i.find('category').text) != None:
            titles_list.append(i.find('title').text)
    return titles_list

def get_dates(get_items):
    stands = {'Jan':'1', 'Feb':'2', 'Mar':'3', 'Apr':'4', 'May':'5', 'Jun':'6',
              'Jul':'7', 'Aug':'8', 'Sep':'9', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
    dates_list = []
    r = re.compile(u'단신&속보')
    for i in get_items:
        if r.search(i.find('category').text) != None:
            imp = i.find('pubdate').text.split(' ')[1:4]
            dates_list.append(imp[2]+'_'+stands[imp[1]]+'_'+imp[0])

    return dates_list

def get_flash():
    from time import localtime, strftime

    items =get_items()
    titles = get_titles(items)
    urls = get_url(items)
    dates = get_dates(items)
    contents =''
    Y_time=strftime("%Y", localtime())
    M_time=int(strftime("%m", localtime())) -1
    if M_time == 0:
        M_time = 12
    Day_time = strftime("%d", localtime())

    in_Week_time = Y_time +'_'+str(M_time)+'_'+ Day_time

    if dates == []:
        return contents

    chk = 0
    len_items = len(dates)
    contents += u'==========한 달 이내===========\n'
    if len_items > 5:
        len_items = 5
    for i in range(0, len_items):
        if in_Week_time <= dates[i]:
            contents += dates[i] + '\n' + titles[i] + '\n' + urls[i] + '\n\n'
            chk = 1
        else:
            if chk == 0:
                contents += u'기사 없음\n'
            contents += u'=============================\n'
            for j in range(i, len_items):
                contents += dates[j] + '\n' + titles[j] + '\n' + urls[j] + '\n\n'
                continue
            break
    return contents