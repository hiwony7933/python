def coffee_machine(button):

    print("뜨거운 물을 준비한다")
    print("종이컵을 준비한다")
    if button == 1:
        print("아메리카노를 탄다")
    elif button == 2:
        print("카페라떼를 탄다")
    elif button == 3:
        print("카푸치노를 탄다")
    else:
        print("아무거나 탄다")
    print("물을 붓는다")
    print("스푼으로 젓는다")

reorder = ""
while reorder != "stop":
    order = int(input("어떤 커피를 드릴까요: (1. 아메리카노 2.카페라떼 3.카푸치노): "))
    nickname = input("이름: ")
    coffee_machine(order)
    print("%s님 커피나왔습니다" % nickname)
    reorder = input("type `stop` to quit: ")
    print("------------------------")
    
