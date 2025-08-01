import sqlite3


# conn = sqlite3.connect('test_sqlite.db')#データベースファイルを作る
conn = sqlite3.connect(':memory:')#何回も作り直す。

curs = conn.cursor()#カーソル

# curs.execute(
#     'CREATE TABLE person(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')#テーブル作成IDと名前を入れるように
# conn.commit()

# curs.execute(
#     'INSERT INTO person(name) values("Mike")'#名前のところに当てはめる
# )
# conn.commit()

# curs.execute('SELECT * FROM person')#テーブルの中身確認
# print(curs.fetchall())

# curs.execute(
#     'INSERT INTO person(name) values("Ikko")'#名前のところに当てはめる
# )
# curs.execute(
#     'INSERT INTO person(name) values("Yoko")'#名前のところに当てはめる
# )
# conn.commit()


# curs.execute('UPDATE person set name = "Michel" WHERE name = "Mike"')#Mikeを書き換えアップデート
# conn.commit()#コミットしないとほんまには書き換えられない。

curs.execute('DELETE FROM person WHERE name = "Michel"')
conn.commit()

curs.execute('SELECT * FROM person')#テーブルの中身確認
print(curs.fetchall())

curs.close()
conn.close#SQL使用終了