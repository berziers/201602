from flask import Flask, jsonify
import psycopg2 as dbapi2

application = Flask(__name__)
db = dbapi2.connect (database="dafambackend", user="ekowibowo", password="")
cur = db.cursor()


@application.route("/login_json/<user>/<password>")
def login_json(user,password):
    print(user,password)
    if user == 'risdyanto' and password == 'abc123':
        hasil = {}
        hasil['login_status'] = 'User diterima'
        hasil['login_sukses'] = True
        return jsonify(hasil)
    else:
        hasil = {}
        hasil['login_status'] = 'User ditolak'
        hasil['login_sukses'] = False
        return jsonify(hasil)

@application.route('/get_users')
def get_users():
    cur.execute ("SELECT id, username, password FROM users");
    rows = cur.fetchall()
    users = []
    for i, row in enumerate(rows):
        users.append({'id': row[0]})
        users.append({'username': row[1]})
        users.append({'password': row[2]})

    return jsonify(data=users)



if __name__ == '__main__':
    application.run(debug=True, port=8080)