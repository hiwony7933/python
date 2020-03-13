# C:/doit/db_select.py
import sqlite3

## 변수 선언 부분 ##
con,cur = None, None
data1, data2, data3, data4 = "", "", "", ""
row = None

## 메인 코드 부분 ##
con = sqlite3.connect("C:/sqlite/naverDB")  # naverDB를 불러오고
cur = con.cursor()      # SQlite와 연결 통로 만들어주고
cur.execute("SELECT * FROM userTable")  # sql문의 userTable이라는 table을 불러오고 전체 열 출력

print("-"*50) # 임의로 시각화 줄표시
print("--------------------------------------------")


while (True):
    row = cur.fetchone()    # DB에 저장된 하나의 row를 불러오고
    if row == None:     # DB에 마지막row가 없으면 break
        break;
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print("%5s %15s %15s %d" % (data1, data2, data3, data4))    # 각 row 순서대로 대입해서 가져옴

con.close( )
