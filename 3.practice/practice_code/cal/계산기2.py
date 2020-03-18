def cal(a,b,c) :
    if c == "+" :
        return a+b
    elif c == "-" :
        return a-b
    elif c == "*" :
        return a*b
    elif c == "/" :
        return a/b

reorder = ""
while reorder != "stop" : 
    order = input("계산구분을 입력要( + - * / ) : ")
    if order == "+" or order == "-" or order == "*" or order == "/" :
        while True :
            number1 = int(input("첫수를 두시오 : "))
            if number1 == "" : continue
            while True : 
                number2 = int(input("두번째를 두시오 : "))
                if number2 == "" : 
                    print("%d %s %d = %0.2f"% (number1, order, number2, cal(number1, number2, order)))
        reorder = input("다시할려면 'enter' 안할꺼면 `stop 입력` : ")
        print("------------------------")
    else :
        print("잘못입력하셨네요")
    
