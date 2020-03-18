class FourCal :
    def setdata(self, first, second) :
        self.first = first
        self.second = second
    def add(self) :
        result = self.first + self.second
        return result

    def add1(self, first1, second1) :
        result = first1 + second1
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

    

a = FourCal()
order=""

while order != "stop" :
    while True : 
        var1 = input("첫번재값")
        if var1.isalpha() or var1 == "" :            # 엔터를 쳤을때
            continue
        
        break

    while True :
        var2 = input("두번째값")
        if var2.isalpha() or var2 == "" :            # 엔터를 쳤을때
            continue
        
        break

    a.setdata(int(var1), int(var2))
    
    if a.div() == "안됨" :
        print("다시해")
        continue                # continue , break, return 실행될때는 아래코드 무시됨으로 else : X
    
    print(a.add(), a.mul(), a.sub(), a.div())

    order = input("입력 stop :") 
    print("="*20)    







