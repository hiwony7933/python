

f = open("D:/python/PJTEuler/add_test.txt", "r")

list_a = []     # 깡통 리스트 만들고
while True :
    line = f.readline()     # 첫줄부터 차례대로 불러와서 추가 시킴
    line = str(line)
    line = line[:50]        # /n 이게 생성되어서 불러와서 50자리까지만 리스트 생성
    list_a.append(line)
    if not line: break      # 마지막줄까지 불러오면 break

# print("문자열의 길이%s 줄" % len(list_a[0]))
# print(len(list_a))    101개의 list 요소 생성됨을 확인함..
f.close()

del list_a[100:]    # txt 파일 읽는 중간에 101번째에 빈칸이 생겨서 지웠음
result = 0
for i in list_a :
    i_list = int(i)     # 리스트 요소들을 정수로 변경해서 누적합
    result = i_list + result
    # print(result)

print("모두다합한값: %s" % result)
result =str(result)     # 앞에 10자리만 알아야하니깐 문자로 전환
result = result[:10]    # 앞 10자리만 출력
print(result)