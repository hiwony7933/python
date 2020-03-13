from selenium import webdriver
import time
import random

randomus = random.random()
randomsl = random.uniform(1, 3)

driver = webdriver.Chrome('/Users/jw/python/chromedriver')
driver.implicitly_wait(3)



driver.get("https://cafe.naver.com/joonggonara/712664803") #내꺼 글 
driver.implicitly_wait(3) # 3초 대기 

driver.find_element_by_xpath('//*[@id="GpVKx"]/table/tbody/tr[1]/td[1]/div/textarea').send_keys('파이썬에서의 매크로ㅎㅇ')
time.sleep(randomsl)
driver.find_element_by_xpath('//*[@id="GpVKx"]/table/tbody/tr[1]/td[2]/div/a').click()

