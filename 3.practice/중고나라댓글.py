from selenium import webdriver
import time
import random

randomus = random.random()
randomsl = random.uniform(1, 3)

driver = webdriver.Chrome('/Users/jw/python/chromedriver')
driver.implicitly_wait(3)

driver.get("https://nid.naver.com/nidlogin.login")

driver.implicitly_wait(3) # 3초 대기 

username = 'tlgudlove111'
userpw = '92ghlrhks'

username2 = list(username)
userpw2 = list(userpw)

for temp in username2 :
    driver.find_element_by_xpath('//*[@id="id"]').send_keys(temp)
    time.sleep(randomus)

time.sleep(randomus)

for temp in userpw2 :
    driver.find_element_by_xpath('//*[@id="pw"]').send_keys(temp)
    time.sleep(randomus)

time.sleep(randomsl)

driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

time.sleep(randomsl)

driver.get("https://section.cafe.naver.com")
driver.implicitly_wait(3) # 3초 대기 

time.sleep(randomsl)

# driver.get("https://cafe.naver.com/joonggonara") #중고나라 페이지
driver.get("https://cafe.naver.com/joonggonara/712664803") #내꺼 글 
driver.implicitly_wait(3) # 3초 대기 

# driver.find_element_by_xpath('//*[@id="comment_text"]').send_keys('파이썬에서의 매크로ㅎㅇ')

driver.find_element_by_xpath('//*[@id="GpVKx"]/table/tbody/tr[1]/td[1]/div/textarea').send_keys('파이썬에서의 매크로ㅎㅇ')
time.sleep(randomsl)
driver.find_element_by_xpath('//*[@id="GpVKx"]/table/tbody/tr[1]/td[2]/div/a').click()









