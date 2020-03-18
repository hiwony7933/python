
class Cal :
    def __init__(self, first, second) :
        self.first = first
        self.second = second

    def rise(self) :
        result = self.first * self.second
        return result 


name = input("이름을 입력하세요 :")
pay = input("기존 연봉을 입력하세요 :")
payup = input("연봉인상율을 입력하세요 : ")


b = Cal(int(pay), int(payup)). rise()

print("%s 의 내년연봉은 %d 만원입니다."%(name, b))
