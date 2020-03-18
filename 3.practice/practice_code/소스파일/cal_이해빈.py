#cal_이해빈.py

#함수값
def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    return(a/b)




#셸노출

while True:
    print("="*22)
    print("1. +\n2. -\n3. X\n4. %")
    print("="*22)
    print()
    menu = input("연산자를 입력해주세요 (+, -, *, /)")
    print()
    numA = int(input("계산할 첫번째 숫자를 입력하세요."))
    numB = int(input("계산할 두번째 숫자를 입력하세요."))
    if (menu == '+'):
        result = add(numA, numB)
        print()
        print("*계산값은 %s %s %s = %s 입니다.*"%(numA,menu,numB,result))
        print()
    elif (menu =='-'):
        result = sub(numA, numB)
        print()
        print("*계산값은 %s %s %s = %s 입니다.*"%(numA,menu,numB,result))
        print()
    elif (menu =='*'):
        result = mul(numA, numB)
        print()
        print("*계산값은 %s %s %s = %s 입니다.*"%(numA,menu,numB,result))
        print()
    elif (menu =='/'):
        result = div(numA, numB)
        print()
        print("*계산값은 %s %s %s = %s 입니다.*"%(numA,menu,numB,result))
        print()
    else:
        print()
        print("연산자를 잘못 입력하였습니다.초기메뉴로 돌아갑니다.")
        print()
