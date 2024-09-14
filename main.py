import requests
import json

#request simple:
url = 'https://rickandmortyapi.com/api/character/2'
r = requests.get(url)
response = r.text

#ahora hay que parsearlo para ver el status :

j=r.json()

status = j['status']


i = 1

while i < 11:
    url= 'https://rickandmortyapi.com/api/character/{}'.format(i)
    r = requests.get(url)
    j = r.json()
    name = j['name']
    status = j['status']
    print('El personaje {} tiene status:  {}'.format(name, status))
    i += 1