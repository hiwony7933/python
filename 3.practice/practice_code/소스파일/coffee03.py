#coffee03.py

## 함수 선언 부분 ##
def coffee_machine(button):
    print("#1. (자동으로) 뜨거운 물을 준비한다.")
    print("#2. (자동으로) 종이컵을 준비한다.")

    if button == '1':
        print("#3. (자동으로) 아메리카노를 탄다.")
    elif button == '2':
        print("#3. (자동으로) 카페라떼를 탄다.")
    elif button == '3':
        print("#3. (자동으로) 카푸치노를 탄다.")
    else:
        print("#3. (자동으로) 주문을 종료합니다.")
        return

    print("#4. (자동으로) 물을 붓는다.")
    print("#5. (자동으로) 스푼으로 젓는다.")

## 메인 코드 부분 ##
while True:
    name = input("닉네임은 무엇입니까?")
    coffee = input("손님, 어떤 커피 드릴까요?(1:아메리카노, 2:카페라떼, 3:카푸치노, 4:주문종료)")
    coffee_machine(coffee)
    if coffee == '1':
        coffeenm = "아메리카노"
    elif coffee == '2':
        coffeenm = "카페라떼"
    elif coffee == '3':
        coffeenm = "카푸치노"
    elif coffee == '4':
        print("주문을 종료합니다.")
        break
    else:
        print("주문 번호를 확인하세요.\n")
        continue

    if name:
        print("%s님~ %s 나왔습니다.\n" % (name, coffeenm))
    else:
        print("%s 시키신분~ %s 나왔습니다.\n" % (coffeenm, coffeenm))
      
