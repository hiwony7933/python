import random

def LottoCR() :
    return random.randint(1,46)

def LottoBA() :
    lotto = []
    num = 0
    i = 0
    while  i < 7 :
        i =i +1
        num = LottoCR()
        
        if lotto.count(num) == 0 :
            lotto.append(num)
            
    num = LottoCR()
    
    if lotto.count(num) == 0 :
        lotto.append(num)

    base = lotto[ : 5 ]
    bonus = lotto[-1 : ]
    print("로또번호 %s 보너스 %s" % (base, bonus))
    

LottoBA()
