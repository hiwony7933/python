import re

p = re.compile('[a-z]+')
a = "life is too short"

result = p.match(a)

print(result.group())
print(result.start())
print(result.end())
print(result.span())

########

result = p.findall(a)
print(result)

# 정규식과 매치되는 모든 문자열을 리스트로 돌려줌
# 많이 쓰일거 같은데???

result = p.finditer(a)
print(result)

for r in result : print(r)

### 결과값 
'''
<re.Match object; span=(0, 4), match='life'>
<re.Match object; span=(5, 7), match='is'>
<re.Match object; span=(8, 11), match='too'>
<re.Match object; span=(12, 17), match='short'>
'''
