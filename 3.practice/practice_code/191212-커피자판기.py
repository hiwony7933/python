
def sul_joo(button) :
    print("\n#3 어서옵셔~ ")
    if button == 1 : 
        print("#4 막걸리 나가요 \n")
    elif button == 2 :
        print("#4 참이슬 나가요 \n")
    elif button == 3 :
        print("#4 처음처럼 나가요 \n")    
    print("#5 부어 \n#6 적셔 \n#7 그날의 피로는 술이지\n")
        
reorder = ""
while reorder != "stop":
    menu = int(input("#1 술 골라골라골라 \n 1.막걸리 \n 2.참이슬 \n 3.처음처럼 \n 주문하세요:"))
    table = int(input("#2 몇번 테이블? : "))
    if menu > 3 :
        print("#4 돈없으면 나~~~가~~~")
        print("#5 그날의 피로는 술인데...")
        break
    sul_joo(menu)
    print("%d번 테이블 주문한거 나왔어~ self다 가지가 \n" % table)
    reorder = input("주문할꺼면 'enter' 안할꺼면 `stop` : ")
    print("------------------------")
    
