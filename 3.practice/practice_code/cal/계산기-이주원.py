def cal(a,b,c) :
    if c == "+" :
        result = a+b
    elif c == "-" :
        result = a-b
    elif c == "*" :
        result = a*b
    elif c == "/" :
        result = a/b
    return result

while True :
    order = input("계산구분을 입력要( + - * / ) : ")
    if order == "+" or order == "-" or order == "/" or order == "*" :
        number1 = int(input("첫수를 두시오 : "))
        number2 = int(input("두번째를 두시오 : "))
        print("%d %s %d = %d"% (number1, order, number2, cal(number1, number2,order)))
        break
    else :
        print("다시해")

