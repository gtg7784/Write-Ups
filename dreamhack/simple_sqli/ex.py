import requests

res = requests.post('http://host1.dreamhack.games:8633//login', data={'userid': 'admin', 'userpassword': ''})

print(res)