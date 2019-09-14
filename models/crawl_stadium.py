from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime,timedelta
import time
import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:Kiennguyen98@cluster0-ic9nh.mongodb.net/test?retryWrites=true&w=majority")
db = client.lichdau
p = db.Ars.find()
real_time = datetime.now()
a = webdriver.Chrome()
a.get('https://www.google.com.vn/?gws_rd=ssl')
time.sleep(1)
e = a.find_element_by_name('q')
for v in p:
    for i in v['matches']:
        if i['time'] > (real_time + timedelta(days=7)) :
            e.send_keys(i['doi'][0]+' vs '+i['doi'][1]+' skysports'+ Keys.ENTER)
            a.find_element_by_xpath('//div[@class="ellip"][1]').click()
            t = a.find_element_by_xpath('//li[@class="match-header__detail-item"][3]').text
            print(t)
            s = a.find_elements_by_xpath('//span[@class="match-head__team-badge"]/img')
            for t in s:
                print(t.get_attribute('src'))
            break