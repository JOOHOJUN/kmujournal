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
    r = re.compile(u'속보')
    for i in get_items:
        if r.search(i.find('title').text) == None :
            url_list.append(i.find('guid').text)

    return url_list

def get_titles(get_items):
    titles_list = []
    r = re.compile(u'속보')
    for i in get_items:
        if r.search(i.find('title').text) == None:
            titles_list.append(i.find('title').text)
    return titles_list

def get_dates(get_items):
    stands = {'Jan':'1', 'Feb':'2', 'Mar':'3', 'Apr':'4', 'May':'5', 'Jun':'6',
              'Jul':'7', 'Aug':'8', 'Sep':'9', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
    dates_list = []
    r = re.compile(u'속보')
    for i in get_items:
        if r.search(i.find('title').text) == None:
            imp = i.find('pubdate').text.split(' ')[1:4]
            dates_list.append(imp[2]+'.'+stands[imp[1]]+'.'+imp[0])

    return dates_list

def get_contents():
    from time import localtime, strftime

    items =get_items()
    titles = get_titles(items)
    urls = get_url(items)
    dates = get_dates(items)
    contents =''
    YM_time=strftime("%Y.%m", localtime())
    Day_time = int(strftime("%d", localtime()))-7
    if Day_time < 10:
        Day_time='0'+str(Day_time)

    in_Week_time = YM_time +'.'+ Day_time

    if dates == []:
        return contents

    for i in range(0,3):
        if in_Week_time < dates[i]:
            contents += titles[i]+ '\n' +dates[i] + '\n' +   urls[i] + '\n\n'
        if i == 0:
            contents += u'\n==============\n'
        contents += titles[i]+ '\n' +dates[i] + '\n' +   urls[i] + '\n\n'
        
    return contents
