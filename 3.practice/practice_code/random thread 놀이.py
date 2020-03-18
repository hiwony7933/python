import random


b = input("입력")     # 멈추고 싶은 수 입력 ( string)
c = len(b)            # 입력된 자리수 확인
d = 10 ** c           # 10 제곱 자리수 max 범위 

class RanNumber :
    def __init__(self, first) :
        self.first = first

    def RanNum(self) :
        while True :
            a = random.randint(1 , d)   # 무한 loop로 1부터~ max 범위 지정
            print(a)                # 진행사항 출력
            if a == int(b) : break      # 멈추고싶은 자리 와 같으면 break


'''
num1 = RanNumber("1번숫자")
num2 = RanNumber("2번숫자")
num3 = RanNumber("3번숫자")
num4 = RanNumber("4번숫자")

th1 = threading.Thread(target = num1.RanNum)
th2 = threading.Thread(target = num2.RanNum)
th3 = threading.Thread(target = num3.RanNum)
th4 = threading.Thread(target = num4.RanNum)

th1.start()
th2.start()
th3.start()
th4.start()

th1.join()
th2.join()
th3.join()
th4.join()
### 돌리지마 ㅋㅋㅋ
'''
