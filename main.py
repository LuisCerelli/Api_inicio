import requests
import json

#request simple:
'''
url = 'https://rickandmortyapi.com/api/character/2'
r = requests.get(url)
response = r.text

#ahora hay que parsearlo para ver el status :

j=r.json()

status = j['status']


i = 1

#while i < 5:
    # url= 'https://rickandmortyapi.com/api/character/{}'.format(i)
    # r = requests.get(url)
    # j = r.json()
    # name = j['name']
    # status = j['status']
    # print('El personaje {} tiene status:  {}'.format(name, status))
    # i += 1

#y ahora lo hacemos por episode con una requests:
url= 'https://rickandmortyapi.com/api/episode/1'
r = requests.get(url)
j = r.json()

#print(j['characters'])

#y la quiero recorrer para extraer el nombre del personaje
personajes = j['characters']
lista_names = list()

for personaje in personajes:
    #print(personaje)
    req = requests.get(personaje)
    js = req.json()
    name = js['name']
    lista_names.append(name)

print(lista_names)    
'''
#ahora lo que busco es que la lista de nombres sea de humanos, por ejemplo:
url= 'https://rickandmortyapi.com/api/episode/1'
r = requests.get(url)
j = r.json()
personajes = j['characters']
lista_names_human = list()
for personaje in personajes:
    #print(personaje)
    req = requests.get(personaje)
    js = req.json()
    name = js['name']
    if js['species'] == 'Human':
        lista_names_human.append(name)

print(lista_names_human) 