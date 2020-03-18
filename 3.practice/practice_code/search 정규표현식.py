import re
p = re.compile('[a-z]+')

m = p.search("python")
print(m)

# 결과값
# <re.Match object; span=(0, 6), match='python'>
# span=(0,6) 은 문자 몇개 찾았다 인거 나타내주는거

m = p.search("3 python")
print(m)
# 결과값
# <re.Match object; span=(2, 8), match='python'>
# 3 이후의 


