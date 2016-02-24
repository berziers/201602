from flask import Flask, jsonify, render_template

application = Flask(__name__)

@application.route("/")
def index():
    return render_template("index.html")

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

if __name__ == '__main__':
    application.run(debug=True,port=8080)