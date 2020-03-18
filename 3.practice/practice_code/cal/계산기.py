


#cal = input("계산구분을 입력하세요:")
#number1 = int(input("첫번째 수를 입력하세요:"))
#number2 = int(input("두번째 수를 입력하세요:"))

#if cal == "+"  :
#    print("%d %s %d = %d"% (number1, cal, number2,number1+number2))
#elif cal == "-" :
#    print("%d %s %d = %d"% (number1, cal, number2,number1-number2))
#elif cal == "*" :
#    print("%d %s %d = %d"% (number1, cal, number2,number1*number2))
#elif cal == "/" :
#    print("%d %s %d = %d"% (number1, cal, number2,number1/number2))


def cal(c, a, b) :
    if c == "+" :
        a+b 
    elif c == "-" :
        a-b 
    elif c == "*" :
        a*b  
    elif c == "/" :
        a/b  
   # else :
   #     break

order = input("계산구분을 입력하세요:")
number1 = int(input("첫번째 수를 입력하세요:"))
number2 = int(input("두번째 수를 입력하세요:"))

print("%d %s %d = %d"% (number1, order, number2))#cal(order, number1, number2)))

#cal(order, number1, number2)
