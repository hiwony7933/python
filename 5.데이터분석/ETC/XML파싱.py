# XML 파싱
# http://www.hani.co.kr/rss/ 에서 item태그의 title만 추출

#데이터 가져오기
import requests
resp = requests.get('http://www.hani.co.kr/rss/')
text = resp.text
#print(text)

import bs4
#트리로 펼쳐내기 
bs = bs4.BeautifulSoup(text, 'lxml-xml')

items = bs.find_all('item')

for item in items: 
    title = item.find('title')
    print(title.getText())
