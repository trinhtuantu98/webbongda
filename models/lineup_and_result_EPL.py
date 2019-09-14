from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome()

#ARSENAL
browser.get('https://en.wikipedia.org/wiki/Arsenal_F.C.')
line_up_ars=[]
time.sleep(3)
for i in range(14):
    s=str('//*[@id="mw-content-text"]/div/table[3]/tbody/tr/td[1]/table/tbody/tr[')
    i=str(i+2)
    s=str(s+i+']')
    browser.find_elements_by_xpath(s)
    all_result = browser.find_elements_by_xpath(s)
    for v in all_result:
        print(v.text)
        line_up_ars.append(v.text)
for i in range(14):
    s=str('//*[@id="mw-content-text"]/div/table[3]/tbody/tr/td[3]/table/tbody/tr[')
    i=str(i+2)
    s=str(s+i+']')
    browser.find_elements_by_xpath(s)
    all_result = browser.find_elements_by_xpath(s)
    for v in all_result:
        print(v.text)
        line_up_ars.append(v.text)
resultArs=[]
browser.get('https://baomoi.com/soccer/d/team/243')
for i in range(5):
    s=str('/html/body/div[2]/div[3]/div/div[4]/div/div[2]/div[2]/div[')
    i=str(10-i)
    s=str(s+i+']')
    browser.find_elements_by_xpath(s)
    all_result = browser.find_elements_by_xpath(s)
    for v in all_result:
        print(v.text)
        resultArs.append(v.text)
with open('arsenal.txt','wt',encoding='utf-8') as f:
    for v in line_up_ars:
        f.write(v+'\n')
    f.write('Kết quả 5 trận gần nhất:\n')
    for v in resultArs:
        f.write(v+'\n')
        


#MU
browser.get('https://en.wikipedia.org/wiki/Manchester_United_F.C.')
line_up_MU=[]
time.sleep(3)
for i in range(16):
    s=str('//*[@id="mw-content-text"]/div/table[7]/tbody/tr/td[1]/table/tbody/tr[')
    i=str(i+2)
    s=str(s+i+']')
    browser.find_elements_by_xpath(s)
    all_result = browser.find_elements_by_xpath(s)
    for v in all_result:
        print(v.text)
        line_up_MU.append(v.text)
for i in range(15):
    s=str('//*[@id="mw-content-text"]/div/table[7]/tbody/tr/td[3]/table/tbody/tr[')
    i=str(i+2)
    s=str(s+i+']')
    browser.find_elements_by_xpath(s)
    all_result = browser.find_elements_by_xpath(s)
    for v in all_result:
        print(v.text)
        line_up_MU.append(v.text)
resultMU=[]
browser.get('https://baomoi.com/soccer/d/team/274')
for i in range(5):
    s=str('/html/body/div[2]/div[3]/div/div[4]/div/div[2]/div[2]/div[')
    i=str(10-i)
    s=str(s+i+']')
    browser.find_elements_by_xpath(s)
    all_result = browser.find_elements_by_xpath(s)
    for v in all_result:
        print(v.text)
        resultMU.append(v.text)

with open('MU.txt','wt',encoding='utf-8') as f:
    for v in line_up_MU:
        f.write(v+'\n')
    f.write('Kết quả 5 trận gần nhất:\n')
    for v in resultMU:
        f.write(v+'\n')
   



#CHELSEA
browser.get('https://en.wikipedia.org/wiki/Chelsea_F.C.')
line_up_Chel=[]
time.sleep(3)
for i in range(13):
    s=str('//*[@id="mw-content-text"]/div/table[3]/tbody/tr/td[1]/table/tbody/tr[')
    i=str(i+2)
    s=str(s+i+']')
    browser.find_elements_by_xpath(s)
    all_result = browser.find_elements_by_xpath(s)
    for v in all_result:
        print(v.text)
        line_up_Chel.append(v.text)
for i in range(13):
    s=str('//*[@id="mw-content-text"]/div/table[3]/tbody/tr/td[3]/table/tbody/tr[')
    i=str(i+2)
    s=str(s+i+']')
    browser.find_elements_by_xpath(s)
    all_result = browser.find_elements_by_xpath(s)
    for v in all_result:
        print(v.text)
        line_up_Chel.append(v.text)
resultChel=[]
browser.get('https://baomoi.com/soccer/d/team/252')
for i in range(5):
    s=str('/html/body/div[1]/div[3]/div/div[4]/div/div[2]/div[2]/div[')
    i=str(9-i)
    s=str(s+i+']')
    browser.find_elements_by_xpath(s)
    all_result = browser.find_elements_by_xpath(s)
    for v in all_result:
        print(v.text)
        resultChel.append(v.text)
with open('chelsea.txt','wt',encoding='utf-8') as f:
    for v in line_up_Chel:
        f.write(v+'\n')
    f.write('Kết quả 5 trận gần nhất:\n')
    for v in resultChel:
        f.write(v+'\n')

 #LIVERPOOL
browser.get('https://en.wikipedia.org/wiki/Liverpool_F.C.')
line_up_Liv=[]
time.sleep(3)
for i in range(15):
    s=str('//*[@id="mw-content-text"]/div/table[5]/tbody/tr/td[1]/table/tbody/tr[')
    i=str(i+2)
    s=str(s+i+']')
    browser.find_elements_by_xpath(s)
    all_result = browser.find_elements_by_xpath(s)
    for v in all_result:
        print(v.text)
        line_up_Liv.append(v.text)
for i in range(15):
    s=str('//*[@id="mw-content-text"]/div/table[5]/tbody/tr/td[3]/table/tbody/tr[')
    i=str(i+2)
    s=str(s+i+']')
    browser.find_elements_by_xpath(s)
    all_result = browser.find_elements_by_xpath(s)
    for v in all_result:
        print(v.text)
        line_up_Liv.append(v.text)
resultLiv=[]
browser.get('https://baomoi.com/soccer/d/team/232')
for i in range(5):
    s=str('/html/body/div[1]/div[3]/div/div[4]/div/div[2]/div[2]/div[')
    i=str(10-i)
    s=str(s+i+']')
    browser.find_elements_by_xpath(s)
    all_result = browser.find_elements_by_xpath(s)
    for v in all_result:
        print(v.text)
        resultLiv.append(v.text)
with open('liverpool.txt','wt',encoding='utf-8') as f:
    for v in line_up_Liv:
        f.write(v+'\n')
    f.write('Kết quả 5 trận gần nhất:\n')
    for v in resultLiv:
        f.write(v+'\n')
    
    

#MC
browser.get('https://en.wikipedia.org/wiki/Manchester_City_F.C.')
line_up_MC=[]
time.sleep(3)
for i in range(12):
    s=str('//*[@id="mw-content-text"]/div/table[6]/tbody/tr/td[1]/table/tbody/tr[')
    i=str(i+2)
    s=str(s+i+']')
    browser.find_elements_by_xpath(s)
    all_result = browser.find_elements_by_xpath(s)
    for v in all_result:
        print(v.text)
        line_up_MC.append(v.text)
for i in range(12):
    s=str('//*[@id="mw-content-text"]/div/table[6]/tbody/tr/td[3]/table/tbody/tr[')
    i=str(i+2)
    s=str(s+i+']')
    browser.find_elements_by_xpath(s)
    all_result = browser.find_elements_by_xpath(s)
    for v in all_result:
        print(v.text)
        line_up_MC.append(v.text)
resultMC=[]
browser.get('https://baomoi.com/soccer/d/team/247')
for i in range(5):
    s=str('/html/body/div[1]/div[3]/div/div[4]/div/div[2]/div[2]/div[')
    i=str(10-i)
    s=str(s+i+']')
    browser.find_elements_by_xpath(s)
    all_result = browser.find_elements_by_xpath(s)
    for v in all_result:
        print(v.text)
        resultMC.append(v.text)
with open('ManCity.txt','wt',encoding='utf-8') as f:
    for v in line_up_MC:
        f.write(v+'\n')
    f.write('Kết quả 5 trận gần nhất:\n')
    for v in resultMC:
        f.write(v+'\n')
    


#Tottenham
browser.get('https://en.wikipedia.org/wiki/Tottenham_Hotspur_F.C.')
line_up_Tot=[]
time.sleep(3)
for i in range(12):
    s=str('//*[@id="mw-content-text"]/div/table[6]/tbody/tr/td[1]/table/tbody/tr[')
    i=str(i+2)
    s=str(s+i+']')
    browser.find_elements_by_xpath(s)
    all_result = browser.find_elements_by_xpath(s)
    for v in all_result:
        print(v.text)
        line_up_Tot.append(v.text)
for i in range(12):
    s=str('//*[@id="mw-content-text"]/div/table[6]/tbody/tr/td[3]/table/tbody/tr[')
    i=str(i+2)
    s=str(s+i+']')
    browser.find_elements_by_xpath(s)
    all_result = browser.find_elements_by_xpath(s)
    for v in all_result:
        print(v.text)
        line_up_Tot.append(v.text)
resultTot=[]
browser.get('https://baomoi.com/soccer/d/team/281')
for i in range(5):
    s=str('/html/body/div[1]/div[3]/div/div[4]/div/div[2]/div[2]/div[')
    i=str(10-i)
    s=str(s+i+']')
    browser.find_elements_by_xpath(s)
    all_result = browser.find_elements_by_xpath(s)
    for v in all_result:
        print(v.text)
        resultTot.append(v.text)
with open('Tottenham.txt','wt',encoding='utf-8') as f:
    for v in line_up_Tot:
        f.write(v+'\n')
    f.write('Kết quả 5 trận gần nhất:\n')
    for v in resultTot:
        f.write(v+'\n')

