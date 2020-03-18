def cal(cal_type, num1, num2):
    if cal_type == '+':
        return num1 + num2
    
    elif cal_type == '-':
        return num1 - num2
    
    elif cal_type == '*':
        return num1 * num2
    
    elif cal_type == '/':
        return int(num1 / num2)


while True:
    cal_type = input('계산 구분을 입력하세요 (+ - * /) : ')
    if cal_type not in ['+', '-', '*', '/']:
        print('잘못된 계산 구분입니다. 다시 입력하세요.')
        continue
    num1 = int(input('첫 번째 수를 입력하세요 : '))

    num2 = int(input('두 번째 수를 입력하세요 : '))
    
    if cal_type == '/' and num2 == 0:
        print('0으로 나눌 수는 없습니다. 다시 처음부터 입력해 주세요.')
        continue

    result = cal(cal_type, num1, num2)
    print(f'계산 결과 {num1} {cal_type} {num2} = {result}')

    reorder = input('계산기를 다시 실행할까요? (Y / N): ')
    if reorder == 'Y':
        continue
    else:
        print('계산기를 종료합니다.')
        break

