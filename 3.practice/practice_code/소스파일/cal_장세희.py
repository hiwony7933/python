
def cal(x, y, cal_index):
    if cal_index == '+':
        return x+y
    elif cal_index == '-':
        return x-y
    elif cal_index == '*':
        return x*y
    elif cal_index == '/':
        return x/y



while True:
    cnt = input("계산을 원하시면 아무키나 눌러주세요\n더이상 계산을 원하지 않으시면 0을 눌러주세요. :: ")
    if cnt == '0':
        break
    else:
        x = int(input("\n첫 번째 수를 입력하세요: "))
        y = int(input("두 번째 수를 입력하세요: "))
        cal_index = input("계산 구분을 입력하세요. (+, -, *, /): ")
        
        if cal_index  == '+' or cal_index  == '-' or cal_index  == '*' or cal_index  == '/':
            
            if x == 0 or y == 0 :
                if cal_index == '/':
                    print("\n0으로 나눌 수 없습니다.\n")
                    continue
                else:
                    pass
                
            z = cal(x, y, cal_index)
            print("\n계산기: %d %s %d = %.2f\n" %(x, cal_index, y, z))
        
        else:    
            print("\n잘못입력했습니다.\n")
            continue
            

