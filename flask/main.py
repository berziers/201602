from flask import Flask, jsonify

application = Flask(__name__)

@application.route("/")
def index():
    return "Hello World!"

@application.route("/hitung_luas_segitiga/<int:alas>/<int:tinggi>")
def hitung_luas_segitiga(alas,tinggi):
    hasil = (alas * tinggi) / 2
    return '<h1> Hasil perhitungan </h1> Luas segitiga = {}'.format(hasil)

@application.route("/hitung_luas_segitiga_json/<int:alas>/<int:tinggi>")
def hitung_luas_segitiga_json(alas,tinggi):
    hasil = {}
    hasil['luas_segitiga'] = (alas * tinggi) / 2
    return jsonify(hasil)

@application.route("/apakabar")
def apakabar():
    return "Apa Kabar.."

@application.route("/help")
def help():
    return "Halaman bantuan.. Tolooonngggg.. :p"

@application.route("/help/bantuan1")
def help_bantuan1():
    return "Halaman bantuan 1"

@application.route("/help/bantuan2")
def help_bantuan2():
    return "Halaman bantuan 2"

@application.route("/perulangan")
def perulangan():
    hasil = ''
    for i in range(1,10):
        hasil = '{}Perulangan ke {}<br/>'.format(hasil,i)
    return hasil

@application.route("/login_json/<user>/<password>")
def login_json(user,password):
    if user == 'risdyanto' and password == 'abc123':
        hasil = {}
        hasil['login_succed'] = True
        return jsonify(hasil)
    else:
        hasil = {}
        hasil['login_succed'] = False
        return jsonify(hasil)

if __name__ == '__main__':
    application.run('0.0.0.0', port=8080)
