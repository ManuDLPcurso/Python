import random
import requests

print("Hola mundo")
print(abs(-223.6))

randomNum= random.randint(3, 10000000)

print(randomNum)
r= requests.get('https://fpaniaguapython.github.io/datos/encuesta_poblacion.csv')
csv_data = r.text
with open('salida.csv',mode='wt',encoding='utf-8') as fichero:
    fichero.write(csv_data)

