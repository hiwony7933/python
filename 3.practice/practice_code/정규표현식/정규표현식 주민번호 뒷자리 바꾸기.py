
'''
data = """

park 800905-1049118
kim 700905-1059119
"""

result = []
for line in data.split("\n") :  #
    word_result = []
    for word in line.split(" ") :
        if len(word) == 14 and word[ : 6].isdigit() and word[ 7 : ].isdigit() :
            word = word[ :6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
    
print("\n".join(result))

'''

# word[ :6].isdigit() 숫자인것이냐로 물어보는거

import re # <-- 정규표현식은 re

data = """

park 800905-1049118
kim 700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")  # \d # 다음에 온 문자를 숫자로 인식해라.
                                    # \d 숫자를 {6} 번 반복해서 찾으라 
print(pat.sub("\g<1>-*******",data))  # \g<1> 첫번째 그룹(\d{6})을 변경해서 data에 저장해라.

