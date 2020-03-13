from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import bs4
import sys
import codecs

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
# 혹은 options.add_argument("--disable-gpu")

# driver = webdriver.Chrome('chromedriver', chrome_options=options)
# 백그라운드작업

driver = webdriver.Chrome(
    '/Users/jw/python/chromedriver', chrome_options=options)

file = codecs.open("text.txt", 'w', encoding="utf-8")

driver.get(
    'https://www.youtube.com/results?search_query=%EB%A7%88%EB%A7%88%EB%AC%B4')

body = driver.find_element_by_tag_name('body')  # 스크롤하기 위해 소스 추출

num_of_pagedowns = 10
#20번 밑으로 내리는 것
while num_of_pagedowns:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)
    num_of_pagedowns -= 1

html = bs4.BeautifulSoup(driver.page_source, 'html.parser')
print(html)

file.write(html)

file.close()

