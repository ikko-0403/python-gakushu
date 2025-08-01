import sqlite3

conn = sqlite3.connect('test_sqlite.db')
curs = conn.cursor()

curs.execute('SELECT * FROM person')
rows = curs.fetchall()

for row in rows:
    print(row)

conn.close()
