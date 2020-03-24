# 네이버 tv 팟에서 과에서 하이퍼링크(a) 태그의 내용 가져오기
import requests

addr = 'https://tv.naver.com/'
resp = requests.get(addr)
# print(resp.text)

#html 파싱을 위한 라이브러리 가져오기 
import bs4
#Dom 객체로 만들기 
bs = bs4.BeautifulSoup(resp.text, 'html.parser')
# 선택자를 이용해서 선택 
tvlist = bs.select('li:nth-child(1) > dl > dt > a > tooltip') 

for temp in tvlist : 
    print(temp.getText())

# a 태그의 내용 가져오기 
li = bs.find_all('a')
# print(li)

# 정규식 (문자열 패턴을 조회하기 위한 식) 모듈 import
import re

for temp in li : 
    #print(temp.getText()) # 태그안의 내용 가져오기 
    #print(temp.attrs['href'])  #key 에러 - href 가 없는 경우도 있음 
    if 'href' in temp.attrs :   #href 속성이 temp.attrs에 있는 경우에만 
        #href 속성에 /wiki/ 로 시작하는 링크의 텍스트와 링크만 출력 
        href = temp.attrs['href']
        # 정규식 생성 - /wiki/ 로 시작하는 
        p = re.compile('^(/wiki/)')
        if p.search(href) != None : 
            print(temp.getText(), ":", href)
