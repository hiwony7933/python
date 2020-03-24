# 웹에서 정적인 데이터를 가져오기 위한 라이브러리를 import
import requests

# 다운로드 받을 URL 만들기
addr = "https://dapi.kakao.com/v2/local/search/category.json?category_group_code=PM9&rect=127.0561466,37.5058277,127.0602340,37.5142554"

#header 만들기
headers = {'Authorization': 'KakaoAK 0ae14c42ae0198bceb42b4e627d3464f'}

resp = requests.get(addr, headers=headers)  # 데이터 가져와서 
text = resp.text
#print(text) # 가져온 데이터는 json 임

import json #json 파싱 모듈을 가져오기 
jsondata = json.loads(text)
# print(type(jsondata)) # 맨 처음 시작이 {} 이므로 dict
# print(jsondata['documents']) #documents 키의 데이터가져오기 - list 

li=[]
# 가져온 배열을 행 단위로 읽어서
for imsi in jsondata['documents'] :
    # print(imsi['address_name'], ':', imsi['place_name'])
    # place_name과 address_name을 가지고 dict를 생성
    d = {'명칭' : imsi['place_name'],'주소':imsi['address_name']}
    li.append(d) #dict를 list에 추가 

# 확인
for temp in li :
    print(temp)
    



