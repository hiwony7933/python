
def coffee(nick):
    while True:
        coffee = input("어떤 커피 드릴까요? (1:아메리카노, 2:카페라떼, 3:카푸치노, 4:안시킨다.:")
          
        if coffee == 1 or coffee == '1':
            drank = '아메리카노'   
            print('아메리카노')      
        elif coffee == 2 or coffee =='2':
            drank = '카페라떼' 
            print('카페라떼')
        elif coffee == 3 or coffee == '3':
            drank = '카푸치노'
            print('카푸치노')
            print()
            
        else:break            
        print("1 뜨거운 물 준비")
        print("2 종이컵 준비")
        print("3 %s를 탄다." % drank)
        print("4 물을 붓는다")
        print("5 스푼으로 젓는다")
        print()
        print("%s님 %s 나왔습니다.맛있게 드세요." %(nick, drank))
        
coffee('환')
        
              



          
    

            
        
        
   
