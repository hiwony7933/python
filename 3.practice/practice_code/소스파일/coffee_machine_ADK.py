def menu():
    print("어떤 커피를 드릴까요?")
    print("1. 아메리카노")
    print("2. 카페라떼")
    print("3. 카푸치노")
    print("주문을 종료하시려면 메뉴를 제외한 키를 입력하세요.")
    menu = input()
    if menu == "1":
        print("아메리카노를 탄다.")
        return 1
    elif menu == "2":
        print("카페라떼를 탄다.")
        return 1
    elif menu == "3":
        print("카푸치노를 탄다.")
        return 1
    else:
        print("안녕히가세요.")
        return 0


while menu():
    print("물을 붓는다.")
    print("스푼으로 젓는다.")
    print("손님 커피 여기있습니다.")
    print()
