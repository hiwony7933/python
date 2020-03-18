#커피 자판기 2탄
def coffee_machine():
    while True:
        coffee = int(input('원하시는  커피를 선택하세요 . 1:아메리카노, 2:카페라떼, 3:카페모카  '))
        name = input('주문하시는 분의 성함을 입력해 주세요 : ')
        pay = input('결제는 어떻게 하시나요? 1:현금, 2:카드, 3:상품권 ')
        point = int(input('포인트 적립 하시나요? 1:Yes, 2:No'))
        if point == 1:
            print('포인트 적립을 했습니다.')
        else :
            print('결제만 진행하겠습니다.')
        print()
        print('▶▶▶주문을 전송 중 입니다.▶▶▶')
        print()

        print('┌───────────┐')

        print('#1. 뜨거운 물을 준비          ')
        print('#2. 종이컵을 준비               ')

        if coffee == 1:
            print('#3. 아메리카노를 만든다.  ')
        elif coffee == 2:
            print('#3. 카페라떼를 만든다.   ')
        elif coffee == 3:
            print('#3. 카페모카를 만든다.   ')
        else :
            print('#3. 맛 없는 커피를 만든다.')

        print('#4. 물을 붓는다.     ')
        print('#5. 스푼으로 젓는다.           ')
        print('└───────────┘')
        print()

        if coffee == 1:
            coffee = '아메리카노'
        elif coffee == 2:
            coffee = '카페라떼'
        else :
            coffee = '카페모카'
            
        print(f'{name}님 주문하신 {coffee}  준비 됐습니다.')
        print('──────────────────')
        print()
        
        opinion = int(input('주문을 하시겠습니까? 1:Yes, 2:No '))
        if opinion == 1:
            continue
        else :
            print('이용해 주셔서 감사합니다.')
            break

coffee_machine()
