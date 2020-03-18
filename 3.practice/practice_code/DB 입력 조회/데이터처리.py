import sqlite3
con = sqlite3.connect("c:/sqlite/naverDB")

cur = con.cursor()
cur.execute("Drop TABLE userTable")

cur.execute("CREATE TABLE userTable (id char(4), userName char(15), email char(15), birthYear int)")
cur.execute("INSERT INTO userTable VALUES('john', 'John Bann','john@naver.com', 1990)")
cur.execute("INSERT INTO userTable VALUES('kim', 'Kim Chi','kim@daum.', 1992)")
cur.execute("INSERT INTO userTable VALUES('lee', 'Lee Pal','lee@paran.com', 1988)")
cur.execute("INSERT INTO userTable VALUES('park', 'Park Su','park@gmail.com', 1980)")

con.commit()
con.close()

