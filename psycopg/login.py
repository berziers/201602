import psycopg2 as dbapi2

db = dbapi2.connect(database = "dafambackend", user = "postgres", password = "bpr123***")
cur = db.cursor()

#clear data
cur.execute ("DELETE FROM pengguna")

#insert data
insert = "insert into pengguna (id, username, password) values('{}','{}','{}')"
cur.execute(insert.format(1, 'ela', 'jugarahasia'))
cur.execute(insert.format(2, 'eko', 'rahasia'))

cur.execute ("SELECT * FROM pengguna");
rows = cur.fetchall()
for i, row in enumerate(rows):
    print("Row ", i, " value = ", row)

db.commit()
cur.close()
db.close()



