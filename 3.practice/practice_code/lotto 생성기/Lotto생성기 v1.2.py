import random

def LottoCR() :
    return random.randint(1,46)

def LottoBA() :
    lotto = []
    num = 0
    i = 0
    while  i < 7 :          # 베이스 번호 6번 돌림
        i = i +1
        num = LottoCR()         # random 번호 num 으로 입력 
        if lotto.count(num) == 0 :      #lotto 리스트에 카운트 
            lotto.append(num)           #lotto 리스트에 생성된 랜덤번호 추가 
            
    num = LottoCR() # 보너스 생성기
    
    if lotto.count(num) == 0 :  # 베이스 번호와 중첩 없기
        lotto.append(num)

    
    base = lotto[ : 5 ]
    base.sort()
    bonus = lotto[-1 : ]
    return("로또번호 %s 보너스 %s" % (base, bonus))
    
k = int(input("몇개살래? :"))


for i in range(k) :
    print(LottoBA())
