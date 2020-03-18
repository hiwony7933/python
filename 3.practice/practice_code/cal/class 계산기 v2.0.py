class FourCal :
    def __init__(self, first, second) :
        self.first = first
        self.second = second

    def add(self) :
        result = self.first + self.second
        return result

    def mul(self) :
        result = self.first * self.second
        return result

    def sub(self) :
        result = self.first - self.second
        return result

    def div(self) :
        if not self.first or not self.second :
            return("안됨")
        else :
            result = self.first / self.second
            return result

class UpFourCal(FourCal) :      #클래스 상속
    def pow(self) :
        result = self.first ** self.second
        return result 


order = ""
while order != "stop" :
    while order != "stop" :
        var1 = input("첫번째값 : ")
        if var1.isalpha() or var1 == "" :
            print("값이 문자입니다. 다시입력")
            continue            

        elif len(var1) >= 4 :       # 제곱에 대한 limit
            order = input("값이 4자리수 이상입니다. 진행하시겠습니까?")
           
        break
    
    while order != "stop" :
        var2 = input("두번째값 : ")
        if var2.isalpha() or var2 == "" :
            print("값이 문자입니다. 다시입력")
            continue            

        elif len(var2) >= 4 :       # 제곱에 대한 limit
            order = input("값이 4자리수 이상입니다. 진행하시겠습니까?")
            
        break
    
    a = FourCal(int(var1), int(var2))
    b = UpFourCal(int(var1), int(var2))         # 상속클래스 값 입력 

    if a.div() == "안됨" :
        print("다시해")
        continue
    
    print("더하면 %d, 곱하면 %d, 빼면 %d, 나누면 %d, 제곱 %d" % (a.add(), a.mul(), a.sub(), a.div(), b.pow()))
    print("add ID : %d" % id(a.add()))      # add의 메모리 ID
    print("pow ID : %d" % id(b.pow()))      # 상속된 pow의 메모리 ID

    
    order = input("입력 stop : ")
    print("=" * 20 )




