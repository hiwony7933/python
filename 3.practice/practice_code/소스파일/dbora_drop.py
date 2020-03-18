# C:/doit/dbora_create.py
import cx_Oracle

#한글 지원 방법
import os
os.putenv('NLS_LANG', '.UTF8')

#연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
con = cx_Oracle.connect('c##user1','master','localhost/orcl')
cur = con.cursor()

cur.execute("DROP TABLE userTable")

con.commit( )
con.close( )
