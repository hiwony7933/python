def coffeemachine(nn, coffee):
    print()
    pay_check = 0
    if coffee == '0':
        print("%s 손님 안녕히 가세요.\n" %nn)
        return 0
    else:
        pay = input("결제 도와드리겠습니다. 1: 현금, 2: 카드")
        if pay == '1':
            
            cash = int(input("현금 받았습니다. \n"))
            pay_check = 0

            if coffee == '1':
                if cash >= 2000:
                    print("거스름돈 %d원 입니다. \n" %(cash-2000))
                else:
                    print("%s 손님 결제 금액이 모자랍니다. \n" %nn)
                    pay_check += 1
                
            else:
                if cash >= 3000:
                    print("거스름돈 %d원 입니다. \n" %(cash-3000))
                else:
                    print("%s 손님 결제 금액이 모자랍니다. \n" %nn)
                    pay_check += 1
        else:
            print("카드 받았습니다. \n")

        cofname = ""
        if pay_check == 0:
            
            print("#1. 뜨거운 물을 준비한다.")
            print("#2. 종이컵을 준비한다.")
    
            if coffee =='1':
                print("#3. 아메리카노를 탄다.")
                cofname = "아메리카노"
        
            elif coffee == '2':
                print("#3. 카페라떼를 탄다.")
                cofname = "카페라떼"
        
            elif coffee =='3':
                print("#3. 카푸치노를 탄다.")
                cofname = "카푸치노"
        
            else:
                print("#3. 아무거나 탄다.")
        
            print("#4. 물을 붓는다.")
            print("#5. 스푼으로 젓는다.")
            print()
            print("%s손님~주문하신 %s 여기 있습니다.\n" %(nn,cofname))
            print(pay_check)







while True:
    bell = input("주문 원하시면 벨을 눌러주세요. 1번: ")
    if bell == '1':
        print("아메리카노: 2000원, 카페라떼: 3000원, 카푸치노: 3000원")
        coffee = input("어떤 커피 드릴까요?(1:아메리카노, 2:카페라떼, 3:카푸치노, 0: 퇴점)")
        nn = input("닉네임은?: ")
        coffeemachine(nn, coffee)
    else:
        break


