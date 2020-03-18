

class calc :
    def __init__(self, a, b, c) :
        self.a = a
        self.b = b
        self.c = c
    def cal(self) :
        if self.c == "+" : result = self.a + self.b
        elif self.c == "-" : result = self.a - self.b
        elif self.c == "*" : result = self.a * self.b
        elif self.c == "/" : result = self.a / self.b
        return result

while True :
    order = input("계산구분을 입력要( + - * / ) : ")
    if order == "+" or order == "-" or order == "/" or order == "*" :
        number1 = int(input("첫수를 두시오 : "))
        number2 = int(input("두번째를 두시오 : "))
        num = calc(number1, number2, order)
        res = num.cal()
        print("%d %s %d = %d"% (number1, order, number2, res))
        break
    else :
        print("다시해")

