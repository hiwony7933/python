import random

def getNumber() :
    return random.randint(1,200)


lotto = []
num = 0

while True :
    start = input("** 행운권 추첨을 시작합니다. **")
    if start == "n" :
        break

    num = getNumber()
    
    if lotto.count(num) == 0 :
        lotto.append(num)

    print(" 당첨번호 : %d" %num)
    print("당첨 굿")
    
