import requests

user = raw_input('User Name : ')
url = 'http://127.0.0.1:8080/login_json/{}'.format(user)
print('Communicating with backend server... please wait...')
r = requests.get(url)
d = r.json()
print('Result from server {}'.format(d['login_status']))