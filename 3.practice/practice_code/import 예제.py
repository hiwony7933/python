import calc

while True :
    oper = input("기호입력")
    if oper == "" : break

    var1 = int(input("첫입력"))
    var2 = int(input("둘입력"))

    if oper == "/" and var2 == 0 :
        print("안됨")
        continue

    cal1 = calc.calc(var1, var2, oper)
    res = cal1.cal()

    print("계산기 : %d %s %d = %d" % (var1, oper, var2, res))
