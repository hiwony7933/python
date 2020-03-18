coffee = input('\nwhat do you want? \n1:americano, 2:latte, 3:cappuccino \n:')
while True:
    if coffee == '1':
        print('americano')
    elif coffee == '2':
        print('latte')
    elif coffee == '3':
        print('cappuccino')
        
    else:
        print('water')
        print('now, get out!')
    break
