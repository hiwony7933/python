
def cal(x,y,z):
    if x == y or x=='y':
        result = ('x + y')                    
    elif x == y or x=='y':
        result = ('x - y')                        
    elif x == y or x=='y':
        result = ('x * y')                        
    elif x == y or x=='y':
        result = ('x / y')
        return('z') 
             
while True:    
    order = input("계산구분을 입력하세요.('+','-','*','/')")                  
    call_list = ('+','-','*','/')                  
    var1 = int(input('첫 수를 두세요.'))
    var2 = int(input('두 수를 두세요.'))   
    result(var1,var2)
    print(result)


    
                     
        
        


