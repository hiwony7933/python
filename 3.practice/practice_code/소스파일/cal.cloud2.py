def cal(tt,fc,sc):
    if tt=='+':
        return fc+sc
    if tt=='-':
        return fc-sc
    if tt=='*':
        return fc*sc
    if tt=='/':
        if sc ==0:
            return 'error'
        return fc/sc


while True:
    tt=str(input("계산 구분을 입력하세요(+,-,*,/):"))
    fc=int(input("첫 번째 수를 입력하세요:"))
    sc=int(input("두번 번째 수를 입력하세요:"))
    result =cal(tt,fc,sc)
    print(result)
