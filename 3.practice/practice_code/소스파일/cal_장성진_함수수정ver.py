#계산기 함수

def cal (x, y, i):
    if  i  == '+' :
        result = x+y
        
    elif  i == '-' :
        result = x-y

    elif  i == '*' :
        result = x*y

    else:
        result = x/y

    return result



# front 노출 부분
cal_list = ('+', '-', '*', '/')

while True:
    print("입력 가능한 값 : +(덧셈), -(뺄셈), *(곱셈), /(나눗셈)")
    i = input("어떤 계산을 할까요? :")
    
    if i in cal_list:
        
        if i != '/':
            var1 = int(input("첫번째 수를 입력하세요 :"))
            var2 = int(input("두번째 수를 입력하세요 :"))
            print("=" *30)
            k = cal (var1, var2, i)
            
        else:
            var1 = int(input("첫번째 수를 입력하세요 :"))
            var2 = int(input("두번째 수를 입력하세요 :"))
            if var1 or var2 =='0':
                print("=" *30)
                k = cal (var1, var2, i)
                
            else :
                print("0은 입력할 수 없습니다")
                continue
            
    else:
        print("잘못 입력했습니다. 입력 가능한 값을 확인하세요")
        print("=" *30)
        continue

    print("%s %s %s 계산 결과는 %s입니다" %(var1,i,var2,k))
    
    print("=" *30)


