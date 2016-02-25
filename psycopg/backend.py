from flask import Flask, jsonify, render_template
import psycopg2 as dbapi2

application = Flask(__name__)
db = dbapi2.connect (database="dafambackend", user="postgres", password="bpr123***")
cur = db.cursor()

@application.route("/")
def index():
    return render_template("index.html")

@application.route("/login_json/<user>/<password>")
def login_json(user,password):
    print(user,password)
    if check_login(user, password):
        hasil = {}
        hasil['login_status'] = 'User diterima'
        hasil['login_sukses'] = True
        return jsonify(hasil)
    else:
        hasil = {}
        hasil['login_status'] = 'User ditolak'
        hasil['login_sukses'] = False
        return jsonify(hasil)

def check_login(username, password):
    query = "select id, username from pengguna where username='{}' and password='{}'".format(username, password)
    print(query)
    cur.execute(query)
    rows = cur.fetchall()
    return len(rows) > 0

@application.route('/get_users')
def get_users():
    cur.execute ("SELECT id, username, password FROM pengguna");
    rows = cur.fetchall()
    users = []
    for i, row in enumerate(rows):
        users.append({'id': row[0]})
        users.append({'username': row[1]})
        users.append({'password': row[2]})

    return jsonify(data=users)

if __name__ == '__main__':
    application.run(port=8080)