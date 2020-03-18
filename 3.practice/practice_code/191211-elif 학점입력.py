score = int(input ("점수를 입력하세요:"))   # 받는 수를 정수로 표현함
if score >=90 : grade = "A"
elif score >=80 : grade = "B"
elif score >=70 : grade = "C"
elif score >=60 : grade = "D"
else : grade = "F"
print("{0}점은 {1}학점입니다.".format(score, grade))  # 기본 포매팅
print(f"{score}점은 {grade}학점입니다.")  # f문자열 포매팅
print("%d점은 %c학점입니다."%(score, grade))   # 기본 포매팅


