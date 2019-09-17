from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from db import insert_lineup,clear_database
doi = [{'name':'Napoli','number':299},{'name':'Liverpool','number':232},
        {'name':'Inter','number':305},{'name':'Dortmund','number':242},
        {'name':'Barce','number':248},{'name':'Lyon','number':370},
        {'name':'leipzig','number':685},{'name':'Chelsea','number':252},
        {'name':'Tot','number':281},{'name':'PSG','number':251},
        {'name':'Real','number':234},{'name':'Bayern','number':246},
        {'name':'MC','number':247},{'name':'Aletico','number':229},
        {'name':'Juv','number':230},{'name':'MU','number':274},
        {'name':'Ars','number':243},{'name':'As roma','number':244},
]
clear_database()
browser = webdriver.Chrome()
while True:
    for o in doi:
        lineup = []
        result = []
        browser.get('https://baomoi.com/soccer/d/team/{}'.format(o['number']))
        time.sleep(5)
        a = browser.find_elements_by_xpath('//div[@class="name large-link player"]/a')
        b = browser.find_elements_by_xpath('//div[@class="position large-link"]/span')
        c = browser.find_elements_by_xpath('//div[@class="number statistic goals available"]')
        d = browser.find_elements_by_xpath('//div[@class="number statistic assists"]')
        e = browser.find_elements_by_xpath('//div[@class="number statistic yellow-cards available"]')
        f = browser.find_elements_by_xpath('//div[@class="number statistic red-cards available"]')
        g = browser.find_elements_by_xpath('//div[@class="photo"]/a/img')
        h = browser.find_elements_by_xpath('//div[@class="shirtnumber"]')
        stt = 0
        for v in range(len(a)):
            lineup.append({})
            lineup[stt]['ten'] = a[v].text
            lineup[stt]['vitri'] = b[v].text
            lineup[stt]['banthang'] = c[v+1].text
            lineup[stt]['assist']= d[v].text
            lineup[stt]['thevang']= e[v+1].text
            lineup[stt]['thedo']= f[v+1].text
            lineup[stt]['ava']=g[v].get_attribute('src')
            lineup[stt]['soao']=h[v+1].text
            stt += 1
        for v in range(6,11):
            result.append(browser.find_element_by_xpath('//div[@class="row row--data row--grey"][{}]'.format(v)).text)
        insert_lineup(o['name'],lineup,result)
        print(o['name'],'xong')
        time.sleep(86400)