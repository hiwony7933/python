# c:/doit/db_create2.py
import sqlite3

con=sqlite3.connect("C:/sqlite/naverDB")
cur = con.cursor( )

cur.execute("DROP TABLE news")
cur.execute("CREATE TABLE news (div char(10), title char(100), writer char(10))")
cur.execute("INSERT INTO news VALUES('정치', 'John Bann', 'ydgil')")

con.commit( )
con.close( )
