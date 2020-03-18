#coffee05.py
def coffee_machine(button):
    button = coffee
    print("#1 뜨거운 물을 준비한다.")
    print("#2 종이컵을 준비한다.")
    if button == '1':
         print("#3 아메리카노를 탄다.")
    elif button == '2':
        print("#3 카페라떼를 탄다.")
    elif button == '3':
        print("#3 카푸치노를 탄다.")
    else:
        print("#3 아무거나 탄다.")

    print("#4 물을 붓는다.")
    print("#5 스푼으로 젓는다.")
    
def coffee_order(name, menu, coffee, ice):
    if  coffee not in ['1','2','3']:
        if ice == 'y':
            print("{0}님 주문하신 아무거나 아이스 나왔습니다.".format(name))
        else:
            print("{0}님 주문하신 아무거나 나왔습니다.".format(name))
    else:
        if ice == 'y':
            print("{0}님 주문하신 아이스 {1} 나왔습니다.".format(name, menu[coffee]))
        else:
            print("{0}님 주문하신 {1} 나왔습니다.".format(name, menu[coffee]))

count = 5
while True:
    name = input("성함을 입력하세요(N입력 시 종료) : ")
    if name == 'N' or name == 'n':
        break
    coffee = input("어떤 커피 드릴까요?(1:아메리카노, 2:카페라떼, 3:카푸치노) : ")
    ice = input("차가운 커피를 드릴까요(y/n으로 선택해주세요) : ")
    menu = {'1':'아메리카노', '2':'카페라떼', '3':'카푸치노'}
    coffee_machine(coffee)
    coffee_order(name, menu, coffee, ice)
    print("남은 수량 : %d잔" % count)
    print("="*60)
    count -= 1
    if count < 0:
        print("판매를 종료 합니다.")
        break


