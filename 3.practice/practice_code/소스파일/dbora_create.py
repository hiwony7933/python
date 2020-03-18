# C:/doit/dbora_create.py
import cx_Oracle

#한글 지원 방법
import os
os.putenv('NLS_LANG', '.UTF8')

#연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
con = cx_Oracle.connect('c##user1','master','localhost/orcl')
#con = cx_Oracle.connect('c##user1/master@localhost/orcl')
cur = con.cursor()

cur.execute("CREATE TABLE userTable (id char(10), userName char(15), email char(15), birthYear int)")

cur.execute("INSERT INTO userTable VALUES('john', 'John Bann', 'john@naver.com', 1990)")
cur.execute("INSERT INTO userTable VALUES('kim', 'Kim Chi', 'kim@daum.', 1992)")
cur.execute("INSERT INTO userTable VALUES('lee', 'Lee Pal', 'lee@paran.com', 1988)")
cur.execute("INSERT INTO userTable VALUES('park', 'Park Su', 'park@gmail.com', 1980)")

con.commit( )
con.close( )
