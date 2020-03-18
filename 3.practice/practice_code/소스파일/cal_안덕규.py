def cal(op, a, b):

    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        return a/b

def menu():
    print("계산 구분을 입력하세요(+, -, *, /)")
    op = input("종료하시려면 (+, -, *, /)를 제외한 키를 입력해주세요 : ")
    if op != "+" and op != "-" and op != "*" and op !="/":
        return ""
    while True:
        a = input("첫 번째 수를 입력하세요 : ")
        if a.isalpha():
            print("숫자를 입력해주세요")
        else:
            a = int(a)
            break


    while True:
        b = input("두 번째 수를 입력하세요 : ")
        if b.isalpha():
            print("숫자를 입력해주세요")
            continue
        b = int(b)
        if op == "/" and b == 0:
            print("0으로 나눌 수 없습니다")
        else:
            break
    return str(a)+","+op+","+str(b)+","+str(cal(op, a, b))


while True:
    string = menu()
    if string == "":
        break;
    string = string.split(",")
    print("%s %s %s = %s입니다." %(string[0], string[1], string[2], string[3]))