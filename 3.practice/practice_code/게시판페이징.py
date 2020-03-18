
def getTotalPage(m, n) :
    if m % n == 0 :
        return m //n
    else :
        return m // n+1
while True  :
    tcnt = int(input("게시물의 총건수 : "))
    pcnt = int(input("페이지당 건수  : "))
    print(getTotalPage(tcnt,pcnt))

