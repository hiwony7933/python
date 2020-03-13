

a = 2**1000
b = str(a)      # 문자열로 바꿔줌
b = list(b)     # 리스트로 저장하기 위해서
print(b)

result = 0
for b_list in b :  # 각 리스트를 한개씩 쭉 돌림
    b_list = int(b_list)        # 문자 > 숫자로 다시 전환
    result = b_list + result    # 돌때마다 더함.
    # print(b_list)

print(result)

