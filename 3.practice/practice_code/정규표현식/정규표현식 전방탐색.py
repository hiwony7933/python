## 전방 탐색
import re

p = re.compile(".+:")    # .+:과 일치하는 문자열로 http: 를 돌려줌
m = p.search("http://googole.com")
print(m.group())


# (?=...) 긍정형 전방 탐색, (?!...) 부정형 전방 탐색

p= re.compile(".+(?=:)")    # : 을 제외하고 돌려줌 
m = p.search("http://goohle.com")
print(m.group())

### 부정형 전방 탐색
p= re.compile(".*[.](?!bat$).*$")    # bat가 아니면 찾으삼 
m = p.search("http:// google.com")   # 매칭되는게 없으니 전체 출력
print(m.group())

