# c:/doit/db_create.py
import sqlite3

con=sqlite3.connect("C:/sqlite/naverDB")
cur = con.cursor( )

cur.execute("DROP TABLE userTable")
cur.execute("CREATE TABLE userTable (id char(10), userName char(15), email char(15), birthYear int)")

#cur.execute("INSERT INTO news VALUES('정치', 'John Bann', 'ydgil')")

con.commit( )
con.close( )
