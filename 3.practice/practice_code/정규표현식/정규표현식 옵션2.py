


import re
p = re.compile("^python\s\w+", re.M)  # re.M , re.MULTILINE

i = re.compile("\spython$", re.M)  # re.M , re.MULTILINE


data = """python one
life is too short python
python two
you need python
python three"""

print(p.findall(data))
# 각각의 라인에서 ^ 첫 문자열이고 $ 는 마지막 문자열  

print(i.findall(data))
