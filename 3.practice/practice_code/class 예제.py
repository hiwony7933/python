

def rise(amt) :
    new_amt = amt * 1.1
    return new_amt

while True :
    name = input("이름 입력")
    if name == "" : break

    pay = int(input("연봉입력"))

    res = rise(pay)
    print("%s 의 내년연봉은 %d 다" %(name, res))
              
