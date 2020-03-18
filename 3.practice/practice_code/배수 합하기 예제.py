

'''
ba= []
num=0
k = 1000 / 3
for i in range(1, int(k)) :
    i = i * 3
    ba.append(i)

'''

result = 0
for n in range(1, 1000) :       # 1 부터 999 까지 n에 대입해서 반복
    if n % 3 == 0 or n % 5 == 0 :   # n을 3으로 나눈 나머지가 0이거나, n을 5로 나눈 나머지가 0이라면 
        result += n

print(result)

'''
result = 0
n = 1
while n < 1000 :
    if ( n % 3 == 0) or (n % 5 == 0) :
        result += n
    n += 1

print(result)

'''
