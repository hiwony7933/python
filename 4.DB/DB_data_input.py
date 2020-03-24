# C:/doit/db_insert.py
import sqlite3  # SQlite에 진입하려면 불러와야됨

## 변수 선언 부분 ##
con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql = ""

## 메인 코드 부분 ##
con = sqlite3.connect("C:/sqlite/naverDB")      # naverDB 를 열기위한 SQlite 연결하고
cur = con.cursor()      # SQlite 진입하기 위한 통로

while (True):
    data1 = input("사용자ID ==> ")
    if data1 == "":     # 사용자 ID가 없으면 정지
        break
    data2 = input("사용자이름 ==> ")
    data3 = input("이메일 ==> ")
    data4 = input("출생년도 ==> ")

    sql = "INSERT INTO userTable VALUES('" + data1 + "', '" + data2 + "', '" + data3 + "', " + data4 + ")"
    # SQL 문서식으로 Table input 값으로 data 지정하여 입력하기
    cur.execute(sql)    # SQL 작성

con.commit( )   # SQlite 저장하고
con.close( )    # SQlite 닫기


