import requests
import json

#request simple:
url = 'https://rickandmortyapi.com/api/character/2'
r = requests.get(url)
response = r.text
print(response)