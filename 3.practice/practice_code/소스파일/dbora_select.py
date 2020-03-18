# C:/doit/dbora_select.py
import cx_Oracle

#한글 지원 방법
import os
os.putenv('NLS_LANG', '.UTF8')

## 변수 선언 부분 ##
con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
row = None

## 메인 코드 부분 ##
con = cx_Oracle.connect('c##user1','master','localhost/orcl')
#con = cx_Oracle.connect('c##user1/master@localhost/orcl')
cur = con.cursor()

cur.execute("SELECT * FROM userTable")
print("--------------------------------------------")
print("사용자ID    사용자이름     이메일   출생연도")
print("--------------------------------------------")

while (True):
    row = cur.fetchone()
    if row == None:
        break;
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]

    print("%5s %15s %15s %d" % (data1, data2, data3, data4))

con.close( )
