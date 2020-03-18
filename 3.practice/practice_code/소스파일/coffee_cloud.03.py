##coffee=0
##
##coffee= int(input("어떤 커피를 드릴까요?(1:아메리카노, 2:카페라떼,3:카푸치노)"))
##
##print()
##print("#1. 뜨거운 물을 준비한다.")
##print("#2. 종이컵을 준비한다.")
##
##if coffee ==1:
##    print("#3. 아메리카노를 탄다.")
##elif coffee ==2:
##    print("#3. 카페라떼를 탄다.")
##elif coffee ==3:
##    print("#3. 카푸치노를 탄다.")
##else:
##    print("#3. 아무거나 탄다.")
##
##print("#4. 물을 붓는다.")
##print("#5. 스푼으로 젓는다.")
##print()
##print("손님~커피 여기 있습니다.")



def coffee_machine():
    button = int(input("버튼을 눌러주세요: 1. 아메리카노 2. 카페라떼 3. 카푸치노 :"))
    name = input("성함이 어떻게 되세요:")
    print()
    print("#1. 뜨거운 물을 준비한다.")
    print("#2. 종이컵을 준비한다.")
    if button ==1:
        print("#3. 아메리카노를 탄다.")
    elif button ==2:
        print("#3. 카페라떼를 탄다.")
    elif button ==3:
        print("#3. 카푸치노를 탄다.")
    else:
        print("#3. 아무거나 탄다.")

    print("#4. 물을 붓는다.")
    print("#5. 스푼으로 젓는다.")
    print()
    print("%s님~커피 여기 있습니다."%name)

while True:
    coffee_machine()
