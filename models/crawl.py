from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime,timedelta
import time
import re
team = []
data = []
date = []
real_time = datetime.now()
a = webdriver.Chrome()
a.get('https://www.google.com.vn/?gws_rd=ssl')
time.sleep(1)
e = a.find_element_by_name('q')
e.send_keys('chelsea'+ Keys.ENTER)
a.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/div/div/div[2]/div/ol/li[1]').click()
time.sleep(10)

all_result = a.find_elements_by_xpath('//*[@id="liveresults-sports-immersive__updatable-team-matches"]/div[@class="OcbAbf"]/div/table/tbody/tr/td/div/div/div/table/tbody/tr/td/div[@class="ellipsisize"]')
for v in all_result:
        if v.text == 'CXĐ':
                l = v.text
        else:
                l = v.find_element_by_xpath('./span[1]').text
        team.append(l)
all_date1 = a.find_elements_by_xpath('//*[@id="liveresults-sports-immersive__updatable-team-matches"]/div[@class="OcbAbf"]/div/table/tbody/tr/td/div/div/div/table/tbody/tr[3]/td[3]/div/div/div[@class="imspo_mt__cmd"]')
for v in all_date1:
        if v.text == 'Ngày Mai':
                data_date = real_time + timedelta(days=1)
        elif ',' in v.text:
                o = v.text.split()
                data_date = datetime.strptime(o[-1]+'/19','%d/%m/%y')
        elif len(v.text) <= 5 :
                data_date = datetime.strptime(v.text+'/19','%d/%m/%y') 
        elif len(v.text) <= 8:
                data_date = datetime.strptime(v.text,'%d/%m/%y') 
        date.append(data_date)
all_date2 = a.find_elements_by_xpath('//*[@id="liveresults-sports-immersive__updatable-team-matches"]/div[@class="OcbAbf"]/div/table/tbody/tr/td/div/div/div/table/tbody/tr[3]/td[3]/div/div/div/div[@ class="imspo_mt__pm-inf imspo_mt__date imso-medium-font"]')
for v in all_date2:
        if v.text == 'Ngày Mai':
                data_date = real_time + timedelta(days=1)
        elif ',' in v.text:
                o = v.text.split()
                data_date = datetime.strptime(o[-1]+'/19','%d/%m/%y') 
        elif len(v.text) <= 5 :
                data_date = datetime.strptime(v.text+'/19','%d/%m/%y') 
        elif len(v.text) <= 8:
                data_date = datetime.strptime(v.text,'%d/%m/%y') 
        date.append(data_date)    
n = (len(team))/2
if n % 2 == 1:
        n += 1  
for v in range(int(n)):
    data.append({})
for v in data:
    v['doi'] = []
i = 0
count = 0
for v in team:
    data[i]['doi'].append(v)
    count += 1
    if count == 2:
        i += 1
        count = 0
i = 0        
for v in date:
    data[i]['time'] = v
    i+= 1

for v in data:
        if v['time'] > real_time:
                print(v)



