

result = 0
f =0
for i in range(1,101) :     # 1~100 까지의 제곱을 구하고
    result = i ** 2
    f = result + f      # 그 제곱을 누적 합 을 하고..

add = 0
h = 0
for j in range(1, 101) :    # 1~100 까지의 합을 구하고
    add += j
    h = add + j
print((add**2) - f)     # 합을 제곱한거에서 - 제곱의 합을 뺌

