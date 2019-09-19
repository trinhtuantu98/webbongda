from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from db import insert_lineup,clear_database
doi = [{'name':'Napoli','number':299,'img':'https://i.pinimg.com/originals/75/b7/aa/75b7aa5eaf8fbdbea944cfd55bff0c34.png'},{'name':'Liverpool','number':232,'img':'https://wallpapercave.com/wp/wp4023373.jpg'},
        {'name':'Inter','number':305,'img':'https://i.pinimg.com/originals/fe/fe/f3/fefef37f68742a8753b521f6d18d4cf6.png'},{'name':'Dortmund','number':242,'img':'https://wallpapercave.com/wp/wp1811922.jpg'},
        {'name':'Barce','number':248,'img':'https://wallpapercave.com/wp/wp2338314.jpg'},{'name':'Lyon','number':370,'img':'https://besthqwallpapers.com/Uploads/25-5-2019/93865/thumb2-olympique-lyonnais-fc-golden-logo-ligue-1-blue-abstract-background-soccer.jpg'},
        {'name':'leipzig','number':685,'img':'https://wallpapercave.com/wp/wp4227620.jpg'},{'name':'Chelsea','number':252,'img':'https://wallpaperplay.com/walls/full/0/d/f/285581.jpg'},
        {'name':'Tot','number':281,'img':'https://3.bp.blogspot.com/-NpcaP87JXyo/XGw0LebTiHI/AAAAAAAAG08/M2xUfUhd5JgCvX-7KgtaY5n_FAgpsWB3gCHMYCw/s1600/tottenham-hotspur-wallpapers.jpg'},{'name':'PSG','number':251,'img':'https://wallpapercave.com/wp/wp1810303.jpg'},
        {'name':'Real','number':234,'img':'https://wallpapercave.com/wp/wp4309152.jpg'},{'name':'Bayern','number':246,'img':'https://www.setaswall.com/wp-content/uploads/2018/04/FC-Bayern-Munich-Wallpaper-22-1920x1080.jpg'},
        {'name':'MC','number':247,'img':'https://wallpaperbro.com/img/111215.jpg'},{'name':'Aletico','number':229,'img':'https://picserio.com/data/out/35/atletico-madrid-wallpaper_2592722.jpg'},
        {'name':'Juv','number':230,'img':'https://wallpapercave.com/wp/wp2426149.jpg'},{'name':'MU','number':274,'img':'https://wallpapercave.com/wp/wp2635347.jpg'},
        {'name':'Ars','number':243,'img':'https://thewallpaper.co//wp-content/uploads/2016/10/the-arsenal-wallpaper-2016-emirates-stadium.jpg'},{'name':'Monaco','number':236,'img':'https://wallpapercave.com/wp/wp2009095.jpg'},
]

browser = webdriver.Chrome()
while True:
    clear_database()
    for o in doi:
        lineup = []
        result = []
        browser.get('https://baomoi.com/soccer/d/team/{}'.format(o['number']))
        a = browser.find_elements_by_xpath('//div[@class="name large-link player"]/a')
        b = browser.find_elements_by_xpath('//div[@class="position large-link"]/span')
        c = browser.find_elements_by_xpath('//div[@class="number statistic goals available"]')
        d = browser.find_elements_by_xpath('//div[@class="number statistic assists"]')
        e = browser.find_elements_by_xpath('//div[@class="number statistic yellow-cards available"]')
        f = browser.find_elements_by_xpath('//div[@class="number statistic red-cards available"]')
        g = browser.find_elements_by_xpath('//div[@class="photo"]/a/img')
        h = browser.find_elements_by_xpath('//div[@class="shirtnumber"]')
        i = browser.find_elements_by_xpath('//div[@class="number statistic appearances available"]')
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
            lineup[stt]['solanrasan'] =i[v+1].text
            stt += 1
        stt = 0
        for v in range(6,11):
            result.append({})
            result[stt]['date']= browser.find_element_by_xpath('//div[@class="row row--data row--grey"][{}]/a/div[@class="date"]/span'.format(v)).text
            result[stt]['league']= browser.find_element_by_xpath('//div[@class="row row--data row--grey"][{}]/a/div[@class="league"]/span'.format(v)).text
            result[stt]['team home']= browser.find_element_by_xpath('//div[@class="row row--data row--grey"][{}]/a/div[@class="team home"]/span'.format(v)).text
            result[stt]['sco']= browser.find_element_by_xpath('//div[@class="row row--data row--grey"][{}]/a/div[@class="sco"]/span'.format(v)).text
            result[stt]['team away']= browser.find_element_by_xpath('//div[@class="row row--data row--grey"][{}]/a/div[@class="team away"]/span'.format(v)).text
            stt += 1
        insert_lineup(o['name'],lineup,result,o['img'])
        print(o['name'],'xong')
    time.sleep(86400)