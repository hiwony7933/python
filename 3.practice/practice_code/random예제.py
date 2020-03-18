import random

b = input("입력")     # 멈추고 싶은 수 입력 ( string)
c = len(b)            # 입력된 자리수 확인
d = 10 ** c           # 10 제곱 자리수 max 범위 
   
while True :
    a = random.randint(1 , d)   # 무한 loop로 1부터~ max 범위 지정
    print(a)                # 진행사항 출력
    if a == int(b) : break      # 멈추고싶은 자리 와 같으면 break
