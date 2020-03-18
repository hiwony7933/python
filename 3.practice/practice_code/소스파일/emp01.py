# emp01.py

## 함수 선언 부분 ##
def rise(amt):
    new_amt = amt * 1.1
    return new_amt


## 메인 코드 부분 ##
while True:
    name = input("이름을 입력하세요: ")
    if name == '': break

    pay = int(input("기존 연봉을 입력하세요 : "))

    res = rise(pay)

    print("%s님의 내년 연봉은 %d 만원 입니다.\n" % (name, res))
