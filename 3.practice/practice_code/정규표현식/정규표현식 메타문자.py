import re

p = re.compile("Crow|Servo")        # |는 or 라는 개념 Crow 나 Servo 찾으라
m = p.match("CrowHello")
print(m)
# 결과값
# <re.Match object; span=(0, 4), match='Crow'>


 # 문자 맨 처음 열 일치 하는거 찾으시오
print(re.search("^Life", "Life is too short"))  # 이건 찾았음 
print(re.search("^Life", "My Life"))    # 이건 못찾음
print(re.search("\ALife", "Life is too short")) # \A 가능함 

# 문자열 맨 끝과 매치한거 찾으시오 
print(re.search("short$", "Life is too short"))     # 찾음
print(re.search("short$", "Life is to short, you need python"))     # None
print(re.search("short\Z", "Life is too short"))    #\Z 가능함.


p = re.compile(r'\bclass\b')        # \b 단어 구분자 \B는 반대의 의미 
print(p.search('no class at all'))  # \b됨 \B 안됨
print(p.search('the declassified alforithm')) # \b안됨.  \B됨



