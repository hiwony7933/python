num1=0
num2=0
operator_all = ['+', '-', '*', '/']

def cal(num1, num2, operator):
    if operator == '+':
        result = num1 + num2 
    elif operator == '-':
        result = num1 - num2 
    elif operator =='*':
        result = num1 * num2 
    elif operator =='/':
        result = num1 / num2  

    return result

def calculator(): 
    while 1==1:
        result = 0

        operator = input("계산 구분을 입력하세요(+ - * /): ")
        if operator not in operator_all:
            print( "에러: 올바른 부호를 입력해 주십시오.")
            continue;

        num1 = int(input ("첫 수: "))
        num2 = int(input ("두번째 수: "))

        if operator == '/' and num2 == 0:
            print("에러: 0으로 나눌 수 없습니다 ")
            continue;
        else:
            result = cal(num1,num2,operator)                  
            print(f"계산기: {num1} {operator} {num2} = {result}")
        go_stop = input("계속 하시겠습니까? Y / N: ")
        if go_stop == 'N':
            break; 
        else:
            continue; 

calculator()


    

    
    

