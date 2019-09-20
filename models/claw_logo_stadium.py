from datetime import datetime,timedelta
import time
import pymongo
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bson.objectid import ObjectId
from db import insert,get_all,clear_data
while True:
    a=get_all()
    datetime_object = datetime.now()
    weeknumber=datetime.date(datetime_object).isocalendar()[1]
    thisweek=[]
    thisweek1=[]
    for v in a:
        match={}
        b=v["time"]
        w=datetime.date(b).isocalendar()[1]
        if w == weeknumber:
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
        e.send_keys(v['team1']+' vs '+v['team2']+' '+'Preview,Live Match'+' skysports'+ Keys.ENTER)
        a.find_element_by_xpath('//*[@id="rso"]/div[@class="bkWMgd"]/div[@class="srg"]/div[1]/div/div/div[1]/a[1]/h3/div').click()
        t = a.find_element_by_xpath('//li[@class="match-header__detail-item"][3]').text
        v['stadium']=t
        s = a.find_elements_by_xpath('//span[@class="match-head__team-badge"]/img')
        v['logo1'] = s[0].get_attribute('src')
        v['logo2'] = s[1].get_attribute('src')
    clear_data()
    insert(thisweek1)
    time.sleep(86400)


    