def cal(ari, a, b):
    if ari == '+':
        return a + b
    elif ari == '-':
        return a - b
    elif ari == '*':
        return a * b
    elif ari == '/':
        return a / b
    else:
        print('you are a fool')

while True:
    a = int(input('type the first value \n:'))
    b = int(input('type the second value \n'))
    ari = input('type the arithmetic \n')
    calculator = cal(ari, a, b)
    print(calculator)