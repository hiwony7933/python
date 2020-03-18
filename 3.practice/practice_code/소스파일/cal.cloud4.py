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
    while True:
          fc=input("첫 번째 수를 입력하세요:")
          if not fc.isnumeric():
                   print("첫번째 수를 제대로 입력 안하셨습니다.") 
                   continue
          break
    fc = int(fc)          
    while True:  
            
          sc=input("두번째 수를 입력하세요:")
          if not sc.isnumeric():
                  print("두번째 수를 제대로 입력 안하셨습니다.")
                  continue
          break
    sc = int(sc) 
    result =cal(tt,fc,sc)
    if result =='error':
        print("0으로 나눌 수 없습니다.")
    else:
        print("계산기 %d %s %d = %f"%(fc, tt, sc,result))
    
