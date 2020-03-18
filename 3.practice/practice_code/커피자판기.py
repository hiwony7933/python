

a = int(input("어떤커피를 줄까\n1.아메리카노\n2.카페라떼\n3.카푸치노\n선택해라:"))

             
def coffee_me(a) :
    while True :
        print("#1 뜨거운 물을 준비")
        print("#2 종이컵을 준비")
        if a == 1 :
            print("#3 아메리카노를 탐")

        elif a == 2 :
            print("#3 카페라테를 탐")
        elif a == 3 :
            print("#3 카푸치노를 탐")

        else :
            print("#3 아무거나 처묵")
        print("#4 물부어")
        print("#5 마셔")
    
    
coffee_me(a)        
