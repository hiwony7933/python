# C:/doit/dbora_insert.py
import cx_Oracle

#한글 지원 방법
import os
os.putenv('NLS_LANG', '.UTF8')

## 변수 선언 부분 ##
con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql = ""

## 메인 코드 부분 ##
con = cx_Oracle.connect('c##user1','master','localhost/orcl')
cur = con.cursor()

while (True):
    data1 = input("사용자ID ==> ")
    if data1 == "":
        break;
    data2 = input("사용자이름 ==> ")
    data3 = input("이메일 ==> ")
    data4 = input("출생년도 ==> ")

    sql = "INSERT INTO userTable VALUES('" + data1 + "', '" + data2 + "', '" + data3 + "', " + data4 + ")"
    cur.execute(sql)

con.commit( )
con.close( )
