# 위키백과에서 하이퍼링크(a) 태그의 내용 가져오기

import re
import bs4
import requests

addr = 'https://ko.wikipedia.org/wiki/%EC%9C%84%ED%82%A4%EB%B0%B1%EA%B3%BC'
resp = requests.get(addr)
# print(resp.text)

#html 파싱을 위한 라이브러리 가져오기
#Dom 객체로 만들기
bs = bs4.BeautifulSoup(resp.text, 'html.parser')
# print(type(bs))

# a 태그의 내용 가져오기
li = bs.find_all('a')
# print(li)

for temp in li:
    #print(temp.getText()) # 태그안의 내용 가져오기
    #print(temp.attrs['href'])  #key 에러 - href 가 없는 경우도 있음
    if 'href' in temp.attrs:  # href 속성이 temp.attrs에 있는 경우에만
        #href 속성에 /wiki/ 로 시작하는 링크의 텍스트와 링크만 출력
        href = temp.attrs['href']
        # 정규식 생성 - /wiki/ 로 시작하는
        p = re.compile('^(/wiki/)')
        if p.search(href) != None:
            print(temp.getText(), ":", href)

