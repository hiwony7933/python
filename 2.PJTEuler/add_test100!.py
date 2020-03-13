

result = 1
for i in range(1,101) :     # 1~100 까지의 곱을 구함
    result = i * result

print(result)
result = str(result)    # list 생성을 위한 문자열로 변경
li = list(result)       # list 요소로 전환

sum = 0
for j in li :
    j_li = int(j)       # 다시 정수로 바꿔주고
    sum = j_li + sum
print(sum)

