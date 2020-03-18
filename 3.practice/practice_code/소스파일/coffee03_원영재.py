
def coffee(nick) :
    while True :
        cof = input("어떤 커피를 드릴까요? 1: 아메리카노, 2: 카페라떼, 3: 카푸치노, 이외의 값: 종료 ")
        if cof == 1 or cof == '1' : name = "아메리카노"
        elif cof == 2 or cof == '2' : name = "카페라떼"
        elif cof == 3 or cof == '3' : name = "카푸치노"
        else : break
        print("1 뜨거운 물 준비")
        print("2 종이컵 준비")        
        print("3 %s를 탄다." % name)
        print("4 물을 붓는다")
        print("5 스푼으로 젓는다")
        print()
        print("%s님 %s 여깄습니다." % (nick, name))


coffee("홍길동")
