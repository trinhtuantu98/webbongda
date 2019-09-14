from flask import Flask, render_template
from datetime import datetime,timedelta
import time
from flask import  request, redirect, url_for,session
import pymongo
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bson.objectid import ObjectId
from db import insert
from db import get_all
client = pymongo.MongoClient("mongodb+srv://admin:Kiennguyen98@cluster0-ic9nh.mongodb.net/test?retryWrites=true&w=majority")
db = client.week

a=get_all()
datetime_object = datetime.now()
weeknumber=datetime.date(datetime_object).isocalendar()[1]
thisweek=[]
thisweek1=[]
for v in a:
    match={}
    b=v["time"]
    w=datetime.date(b).isocalendar()[1]
    if w==weeknumber:
        match['team1']=v["team1"]
        match["team2"]=v["team2"]
        match["time"]=v["time"]
        thisweek.append(match)
for v in thisweek:
    m=v["time"]
    n=m.weekday()
    if n==1:
        thisweek1.append(v)
for v in thisweek:
    m=v["time"]
    n=m.weekday()
    if n==2:
        thisweek1.append(v)
for v in thisweek:
    m=v["time"]
    n=m.weekday()
    if n==3:
        thisweek1.append(v)
for v in thisweek:
    m=v["time"]
    n=m.weekday()
    if n==4:
        thisweek1.append(v)
for v in thisweek:
    m=v["time"]
    n=m.weekday()
    if n==5:
        thisweek1.append(v)
for v in thisweek:
    m=v["time"]
    n=m.weekday()
    if n==6:
        thisweek1.append(v)
for v in thisweek:
    m=v["time"]
    n=m.weekday()
    if n==0:
        thisweek1.append(v)

a = webdriver.Chrome()
for v in thisweek1:
    a.get('https://www.google.com.vn/?gws_rd=ssl')
    time.sleep(1)
    e = a.find_element_by_name('q')
    e.send_keys(v['team1']+' vs '+v['team2']+' '+'livematch'+' skysports'+ Keys.ENTER)
    a.find_element_by_xpath('//div[@class="ellip"][1]').click()
    t = a.find_element_by_xpath('//li[@class="match-header__detail-item"][3]').text
    v['stadium']=t
    s = a.find_elements_by_xpath('//span[@class="match-head__team-badge"]/img')
    v['logo1'] = s[0].get_attribute('src')
    v['logo2'] = s[1].get_attribute('src')

insert(thisweek1)

 