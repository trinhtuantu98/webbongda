from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime,timedelta
from db import insert_data,clear_data2
import time
import re
team = ['MU','Ars','MC','leipzig','Atletico','Barce','Bayern','Chel','Dortmun','Inter','Juv','Liv','Monaco','Napoli','PSG','Real','Lyon','Tot']
browser = webdriver.Chrome()
while True:
    so_team = 0
    clear_data2()
    for o in team:
        data = []
        thoigian = []
        stt=0
        browser.get('https://www.google.com.vn/?gws_rd=ssl')
        search  = browser.find_element_by_name('q')
        search.send_keys(team[so_team]+' fixture sky sports'+ Keys.ENTER)
        browser.find_element_by_xpath('//*[@id="rso"]/div/div/div[1]/div/div/div[1]/a[1]').click()
        if so_team == 0:
            time.sleep(5)
            browser.find_element_by_xpath('//*[@id="Accept"]').click()
            time.sleep(5)
        ngay = browser.find_elements_by_xpath('//h4[@class="fixres__header2"]')
        for v in ngay:
            thoigian.append(v.text)
        gio = browser.find_elements_by_xpath('//span[@class="matches__date"]')
        for v in range(len(gio)):
            thoigian[v] = thoigian[v]+' '+gio[v].text
        thang = ['February','May','April','March','January']
        for v in range(len(gio)):
            data.append({})
        for v in thoigian:
            a = v.split()
            k =re.sub(r'\D','',a[1])
            if a[2] in thang:
                j = a[0]+' '+k+' '+a[2]+' '+a[3]+' 20'
            else:
                j = a[0]+' '+k+' '+a[2]+' '+a[3]+' 19'
            date = datetime.strptime(j,'%A %d %B %H:%M %y') + timedelta(hours=6)
            data[stt]['time'] = date
            stt += 1
        team1 = browser.find_elements_by_xpath('//span[@class="matches__item-col matches__participant matches__participant--side1"]/span/span')
        team2 = browser.find_elements_by_xpath('//span[@class="matches__item-col matches__participant matches__participant--side2"]/span/span')
        stt = 0
        for v in range(len(team1)):
            data[stt]['doi'] = []
            data[stt]['doi'].append(team1[v].text)
            data[stt]['doi'].append(team2[v].text)
            stt += 1
        insert_data(team[so_team],data)
        print(team[so_team],'xong')
        so_team += 1
    time.sleep(86400)