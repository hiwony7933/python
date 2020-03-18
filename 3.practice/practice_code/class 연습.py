class FourCal :
    def __init__ (self, first, second) : #def setdata랑 같이 해주면 , init 이 제일먼저 
        self.first = first
        self.second = second
        
    #def setdata(self, first, second) :
    #    self.first = first
    #    self.second = second
        
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
        result = self.first / self.second
        return result
    lastname = "김"

#a = FourCal(4,2)
#a.setdata(4,2)     # __init__ 을 쓰면 setdata 안써도됨.
#print(a.add())
#print(a.mul())
#print(a.sub())

# 기능 추가 라고 생각하면됨.
class MoreFourCal(FourCal) :
    def pow(self) :
        result = self.first ** self.second  
        return result

a=MoreFourCal(4,2)
print(a.pow())

class SafeFourCal(FourCal) :
    def div(self) :
        if self.second == 0 :       # 나누는값이 0인경우 , 숫자 0을 돌려주세요 .
            return 0
        else :
            return self.first /self.second


print(FourCal.lastname)

FourCal.lastname = "박"          # class 변수 바꾸기 
print(FourCal.lastname)


























