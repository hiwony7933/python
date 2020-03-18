#def add_and_mul(a,b,c) :     # add_and_mul 라는 함수를 지정하고 형식은(a,b,c)
#    return a+b+c, a*b*c, a-b-c     # 각각의 연산 을 하고 빠져나감.
#result = add_and_mul(3,4,5)
#print(result)

#def say_nick(nick):             # say_nick 이라는 함수를 지정하고 
#    if nick == "바보" : return   # nick = 바보 면 함수에서 빠져나가라 
#    print("나의 별명은 %s 입니다." % nick)   
#say_nick("바보")

#def say_myself(name, old, man=True):   # 남자를 기본적인 참으로 해놨음. 초기값은 맨 뒤로 
#    print("나의 이름은 %s 입니다."%name)
#    print("나이는 %d살입니다."%old)
#    if man:                 # 남자가 기본 참이기 때문에 기본출력은 "남자다"
#        print("남자다")         
#    else :
#        print("여자다")
#say_myself("이주원", 35, False)        # False로 하면 else 여자 로 



#a = 1
#def vartest() :
#    global a        #함수 밖의 변수를 불러와서 사용함. 사용않하는게 좋다 
#    a = a + 1
#vartest()
#print(a)


#add = lambda a, b : a+b
#result = add(3,4)
#print(result)

#def is_odd(number) :
#    if number % 2 == 1:
#        return True
#    else :
#        return False 


#is_odd = lambda number : "홀수" if number % 2 == 1 else "짝수" 
#print(is_odd(3))




















