#coffee03.py


while True:
    coffee = int(input("\n메뉴를 선택해주세요\n\n1. 아메리카노 2. 카페라떼 3. 카푸치노 4. 카페모카 5.흑당라떼 6. 주문종료 : "))
    if coffee not in [1,2,3,4,5,6]:
        print()
        print("  !! 번호를 다시 입력해주세요  !!   ")
        print()
        continue
    elif coffee == 6:
        print("\n이용해주셔서 감사합니다 ")
        break

    print()
    temp = int(input("1. Hot 2. Iced : "))
    if temp not in [1,2]:
        print()
        print("  !!  번호를 다시 입력해주세요  !!  ")
        print()
        continue
    print()
    shots = int(input("샷추가를 하시겠습니까?\n\n 1. 예 2. 아니오 : "))
    print()
    sugar = int(input("당도를 설정해 주세요\n\n 1. 기본 2. 30% 3. 50% : "))
    print()
    nick = input("닉네임을 입력하세요 : ")

    print()
    print("------------------- 레시피 -------------------")
    print()
    print("#1. 샷을 지정된만큼 넣는다.")


    if coffee ==1 and temp == 1:
         print("#2. 물을 넣는다.")
    elif coffee ==1 and temp == 2:
        print("#2. 물을 넣는다.")
        print("#3. 얼음을 넣는다.")
    elif coffee == 2 and temp == 1:
        print("#2. 우유를 붓는다.")
        print("#3 우유 거품을 낸다.")
    elif coffee == 2 and temp == 2:
        print("#2. 우유를 붓는다.")
        print("#3 우유 거품을 낸다.")
        print("#4. 얼음을 넣는다.")
    elif coffee == 3 and temp == 1:
        print("#2. 우유를 넣는다")
        print("#3. 우유 거품을 많이 낸다.")
    elif coffee == 3 and temp == 2:
        print("#2. 우유를 넣는다")
        print("#3. 우유 거품을 많이 낸다.")
        print("#4. 얼음을 넣는다.")
    elif coffee == 4 and temp == 1:
        print("#2. 우유를 넣는다")
        print("#3. 초코 시럽을 넣는다.")
    elif coffee == 4 and temp == 2:
        print("#2. 우유를 넣는다")
        print("#3. 초코 시럽을 넣는다.")
        print("#4. 얼음을 넣는다.")
    elif coffee == 5 and temp == 1:
        print("#2. 우유를 넣는다")
        print("#3. 흑당시럽을 넣는다.")
    elif coffee == 5 and temp == 2:
        print("#2. 우유를 넣는다")
        print("#3. 흑당시럽을 넣는다.")
        print("#4. 얼음을 넣는다.")

    if coffee == 1: coffee = "아메리카노"
    elif coffee == 2: coffee = "카페라떼"
    elif coffee == 3: coffee = "카푸치노"
    elif coffee == 4: coffee = "카페모카"
    elif coffee == 5: coffee = "흑당라떼"

    if temp == 1: temp = "Hot"
    elif temp == 2: temp = "Iced"

    if shots == 1 : shots = "(샷추가)"
    elif shots == 2 : shots = ""

    if sugar == 1 : sugar = ""
    elif sugar == 2 : sugar = "(당도30%)"
    elif sugar == 3 : sugar = "(당도50%)"

    print()
    print("****** %s님~ 주문하신 %s %s%s%s 나왔습니다. ******" %(nick,temp,coffee,shots,sugar))
    print()

    continue

