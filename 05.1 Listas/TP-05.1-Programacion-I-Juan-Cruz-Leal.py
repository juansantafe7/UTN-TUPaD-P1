import math

#Ejercicio 1
"""
Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
range
    
"""
# Usamos range con paso 4 y convertimos a lista
lista_multiplos = list(range(4, 101, 4))
print(lista_multiplos)

#Ejercicio 2
"""
Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
indexing con números negativos!
    
"""
# Usamos indexación negativa para acceder al penúltimo elemento
cosas_favoritas = ["pizza", "gatos", "coding", "música", "series"]
print(cosas_favoritas[-2])


#Ejercicio 3
"""
Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
ejemplo:
lista_vacia = []
    
"""
# Utilizamos append para añadir elementos a una lista vacía
lista_vacia = []
lista_vacia.append("sol")
lista_vacia.append("mar")
lista_vacia.append("arena")
print(lista_vacia)



#Ejercicio 4
"""
Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
en los videos o bien investigar cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"]
    
"""
# Se modifican valores específicos usando índices, incluyendo negativos
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)


#Ejercicio 5
"""
Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
    
"""

"""
El programa crea una lista llamada numeros con los valores [8, 15, 3, 22, 7]
Busca el número más grande de la lista usando max(numeros) (En este caso, el número más grande es 22)
Elimina ese número de la lista usando remove(max(numeros))
Imprime la lista resultante, que es [8, 15, 3, 7]

"""


#Ejercicio 6
"""
Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
pantalla los dos primeros.
    
"""
# Creamos una lista llamada lista_numeros utilizando range(10, 31, 5), la cual genera números desde el 10 hasta
# el 30 , aumentando 5 en 5
# Usamos slicing [:2] para mostrar sólo los 2 primeros números

lista_numeros = list(range(10, 31, 5))
print(lista_numeros[:2])


#Ejercicio 7
"""
Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
    
"""
# Se reemplazan los índices 1 y 2 por nuevos valores con slicing
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["camioneta", "coupe"]
print(autos)


#Ejercicio 8
"""
Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
directamente. Imprimir la lista resultante por pantalla.
    
"""
# Creamos la lista vacía dobles = []
# Multiplicamos por 2 y usamos append para agregar los elementos
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)


#Ejercicio 9
"""
Dada la lista “compras”, cuyos elementos representan los productos comprados por
diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
a) Agregar "jugo" a la lista del tercer cliente usando append.
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
c) Eliminar "pan" de la lista del primer cliente.
d) Imprimir la lista resultante por pantalla
    
"""
# Se modifica cada sublista accediendo por índice
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) se agrega "jugo"
compras[2].append("jugo")

# b) se reemplaza "fideos" por "tallarines"
compras[1][1] = "tallarines"

# c) se elimina "pan"
compras[0].remove("pan")

print(compras)


#Ejercicio 10
"""
Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
● Posición lista_anidada[0]: 15
● Posición lista_anidada[1]: True
● Posición lista_anidada[2][0]: 25.5
● Posición lista_anidada[2][1]: 57.9
● Posición lista_anidada[2][2]: 30.6
● Posición lista_anidada[3]: False
Imprimir la lista resultante por pantalla
    
"""
# Se crea la lista la cual incluye enteros, booleanos y una lista anidada con tres valores flotantes
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]

print(lista_anidada)
