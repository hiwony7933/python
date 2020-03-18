import re
p = re.compile("a.b")
m= p.match('a\nb')
print(m)

#### 이렇게 하면 결과값은 None이 된다.
## \n 으로 인하여 매치가 안됨

p = re.compile('a.b', re.S)     # 대문자 S 혹은 re.DOTALL 가능함. 
m = p.match("a\nb")
print(m)

# 이렇게 하면 \n도 하나의 문자열로 같이찾아준다 .
# 결과값
# <re.Match object; span=(0, 3), match='a\nb'>


p = re.compile('[a-z]', re.I)  # 영어 아이 <-
r=p.match("python")
print(r)
f=p.match("Python")
print(f)
v=p.match("PYTHON")
print(v)

# 결과값은 대.소문자에 관계없이 매치함.
# 결과값 
# <re.Match object; span=(0, 1), match='P'>
