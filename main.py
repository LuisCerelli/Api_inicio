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
lista_names_other = list()

for personaje in personajes:
    #print(personaje)
    req = requests.get(personaje)
    js = req.json()
    name = js['name']
    if js['species'] == 'Human':
        lista_names_human.append(name)
    else:
        lista_names_other.append(name)

print(f"La lista de los nombres de seres humanos es: \n{'\n'.join(lista_names_human)}") 
print(f"En cambio, la lista de los seres NO humanos es:\n {'\n'.join(lista_names_other)}")

#otra forma de imprimir tipo columna y que los nombres no salgan uno abajo del otro es: 
print("La lista de los nombres humanos es: ")
for name in lista_names_human:
    print(name)

print("\nEn cambio, la lista de los seres NO humanos es: ")
for name in lista_names_other:
    print(name)