myid = "python"
mypw = "1234"

ID = ""
PW = ""
a = 0
b = 5    #  
while a < b :
    a = a + 1
    if myid != ID :
        ID = input("ID 입력 : ")
    if mypw != PW :
        PW = input("PW 입력 : ")
    if ID == myid and PW == mypw :
        print("정상적으로 로그인에 성공했습니다.")
        break
    elif myid != ID and mypw == PW :
        print("아이디가 틀렸습니다.")
    elif myid == ID and mypw != PW :
        print("패스워드가 틀렸습니다.")
    else :
        print("아이디와 패스워드가 %d회 틀렸습니다." % a)




