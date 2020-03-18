def cal(tt,fc,sc):
        if tt=='+':
            return fc+sc
        elif tt=='-':
            return fc-sc
        elif tt=='*':
            return fc*sc
        elif tt=='/':
            if sc ==0:
                return 'error'
            return fc/sc
       
a =( '+','-','*','/')
while True:
    tt=str(input("계산 구분을 입력하세요(+,-,*,/):"))
    if tt not in a:
        print('stop')
        break
    fc=int(input("첫 번째 수를 입력하세요:"))
    sc=int(input("두번 번째 수를 입력하세요:"))
    result =cal(tt,fc,sc)
    if result =='error':
        print("0으로 나눌 수 없습니다.")
    else:
        print("계산기 %d %s %d = %f"%(fc, tt, sc,result))
    
