import psycopg2 as dbapi2

def check_login(username, password):
    query = "select id, username from users where username='{}' and password='{}'".format(username, password)
    cur.execute(query)
    rows = cur.fetchall()
    return len(rows) > 0

db = dbapi2.connect (database="dafambackend", user="ekowibowo", password="")
cur = db.cursor()

#clear data
cur.execute ("DELETE FROM users")

#insert data
insert = "insert into users(username, password) values('{}','{}')"
cur.execute(insert.format('ela', 'jugarahasia'))
cur.execute(insert.format('eko', 'rahasia'))

print(check_login('eko', 'rahasia'))

cur.execute ("SELECT * FROM users");
rows = cur.fetchall()
for i, row in enumerate(rows):
    print("Row", i, "value = ", row)


db.commit()
cur.close()
db.close()