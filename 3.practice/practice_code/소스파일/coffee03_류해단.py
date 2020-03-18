#coffee03
import re 
coffee = 0
totalCount = 0

#커피주문 
def coffee_machine(botton,money,nickname,cnt,totalCount):
    print()
    print("#1.뜨거운 물을 준비한다.")
    print("#2.종이컵을 준비한다.")

    if botton == '1':
        print("#3.아메리카노를 탄다.")
    elif botton == '2':
        print("#3.카페라떼를 탄다.")
    elif botton == '3':
        print("#3.카푸치노를 탄다.")
    else:
        print("#3.아무거나 탄다.")

    print("#4.물을 붓는다.")
    print("#5.스푼으로 젓는다.")
    print()
    totalCount -= cnt
    if money:
        print("%s ~ 커피 여기 있습니다.%d잔 드리겠습니다.거스름돈 %d 입니다." % (nickname,cnt,money))
    else:
        print("%s ~ 커피 여기 있습니다.%d잔 드리겠습니다." % (nickname,cnt))
        
    return totalCount



#받아야 할 금액
def rev_coffee_price(botton,cnt):
    price = 0
    if botton == '1':
        price = 4100*cnt
    elif botton == '2':
        price = 4200*cnt
    elif botton == '3':
        price = 4300*cnt
    else:
        price = 4500*cnt
    return price



while True:

    #최초 기동시 총 잔수 조회
    while totalCount == 0:
        try:
            totalCount = int(input("영업을 시작합니다.총 몇잔 할 예정입니까? "))
        except ValueError :  # 에러 종류
            print('숫자만 입력 가능합니다.'.format(cnt))
            continue
        if totalCount > 0:
            break

    #1. 커피주문
    coffee = input("어떤 커피 드릴까요 ?(1:아메리카노, 2:카페라떼,3:카푸치노) ")
    if coffee not in ('1','2','3'):
        print("주문을 확인하여주십시요.")
        continue
    
    #2. 이름 입력
    nickname = input("Nick name입력하여 주십시요.? ")

    #3. 개수
    cnt= 0
    while True:
        try:
            cnt = int(input("몇잔 주문드립니까? "))
            if cnt > totalCount:
                print("%d잔 이상 주문이 안됩니다." % totalCount)
                continue
        
        except ValueError :  # 에러 종류
            print('숫자만 입력 가능합니다.'.format(cnt))
            continue
        if cnt > 0:
            break
     
    price = rev_coffee_price(coffee,cnt)
    rev_price = int(input("%d원 결재 부탁드립니니다. " % price))
    money = rev_price - price
    if money < 0:
        print("잔액이 부족합니다.")
    else:
        totalCount = coffee_machine(coffee,money,nickname,cnt,totalCount)

        
    #커피가 떨어졌을 경우
    if totalCount == 0:
        print("커피가 떨어졌습니다.")
        print("더이상 주문이 불가합니다.")
        print("영업을  종료하겠습니다.")
        break

