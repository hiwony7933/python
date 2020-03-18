#coffee_machine.py

##함수 부분##
def coffee_machine(coffee):
       print()
        print("#1. 뜨거운 물을 준비한다.")
        print("#2. 일회용컵을 준비한다.")
        if coffee ==1:
            print("#3. 일회용컵에 샷 투척.")
        elif coffee == 2:
            print("#3. 일회용컵에 샷+따뜻한우유 투척.")
        elif coffee == 3:
            print("#3. 일회용컵에 샷+따뜻한우유+시나몬 투척.")
        if coffee ==4:
            print("#3. 일회용컵에 고구마가루+따뜻한우유 투척.")
        else:
            print("#3. 손가락을 담군다.")
            
        print("#4. 뜨거운 물을 붓는다.")
        print("#5. 손가락으로 젓는다.")
        print()

##본문 부분##
while True:
        nick=input("닉네임을 입력해주세요.")
        print()
        coffee = 0
        coffee = int(input("Would you like something drink?(1:아메리카노, 2:카페라떼, 3:카푸치노,4:고구마라떼)"))
        if 
            coffee_machine(coffee)
        print("%s야~음료 나왔다."%nick)
        print()

        continue

                
           


