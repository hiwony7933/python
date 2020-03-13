import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import random

randomus = random.random()
randomsl = random.uniform(1, 3)

driver = webdriver.Chrome('/Users/jw/python/chromedriver')
driver.implicitly_wait(3)
driver.get("https://www.naver.com")


sourcecode = urllib.request.urlopen("https://www.naver.com").read()
soup = BeautifulSoup(sourcecode, "html.parser")
list = []
for naver_text in soup.find_all("span", class_="ah_k"):
    list.append(naver_text.get_text())
    print(list)




