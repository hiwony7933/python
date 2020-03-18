import random
def coffee_machine():
    while True:
        button = input("어떤 커피 드릴까요?(1:아메리카노, 2:카페라떼, 3:카푸치노, 4:나가기)")
        if button == '4':
            return
        name = input("이름을 알려주세요!:")
        print()
        print("#1. 뜨거운 물을 준비한다.")
        print("#2. 종이컵을 준비한다.")
        print("")

        if not (button=='1' or button=='2' or button=='3'):
            print("##. 아무거나 선택한다.")
            button=str(random.randint(1,3))
            
        if button=='1':
            print("#3. 아메리카노를 탄다.")
            coffee = '아메리카노'
        elif button=='2':
            print("#3. 카페라떼를 탄다.")
            coffee = '카페라떼'
        elif button=='3':
            print("#3. 카푸치노를 탄다.")
            coffee = '카푸치노'
        

        print("#4. 물을 붓는다.")
        print("#5. 스푼으로 젓는다.")
        print()
        print("{0}님~ {1} 여기 있습니다.".format(name, coffee))
        
coffee_machine()
