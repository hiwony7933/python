import re
p = re.compile('[a-z]+')

m = p.match("python")
print(m)

# 결과값
# <re.Match object; span=(0, 6), match='python'>
# span=(0,6) 은 문자 몇개 찾았다 인거 나타내주는거

m = p.match("3 python")
print(m)
# 결과값
# None
# 3과 빈칸이 match 되는게 없다 . a~z 까지를 찾아달라고 햇기때문에



p = re.compile('\s[a-z,0-9]+')  # 정규표현식을 넣고 
m = p.match(" 2039python") # 조사할 문자열 넣고 

if m :
    print("Match Found: ", m.group())
else :
    print("No match")
    
