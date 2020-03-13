import random
import time
import datetime

dt = datetime.datetime.now()
print(dt)

randomsl = random.uniform(1, 3)

randomus = random.random()

print(randomus)
# i =[]
# for i in range(1,10,1) : 
#     a = random.uniform(1, 3) 
#     print(a)
#     time.sleep(a)
#     i=i+1


# username = 'tlgudlove111'

# username2 =list(username)

# print(username2)


# for temp in username2 :
#     print(temp)
#     driver.find_element_by_xpath('//*[@id="id"]').send_keys(temp)
#     time.sleep(randomsl)

import urllib.request
from bs4 import BeautifulSoup

def main():
    sourcecode = urllib.request.urlopen("http://www.naver.com").read()
    soup = BeautifulSoup(sourcecode, "html.parser")
    list = []
    for naver_text in soup.find_all("span", class_="ah_k"):
        list.append(naver_text.get_text())
    print(list)

if __name__ == "__main__":
    main()


