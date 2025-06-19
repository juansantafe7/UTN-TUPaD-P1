# Ejercicio 1 - Añadir frutas a un diccionario
import math

#Ejercicio 1
"""
Dado el diccionario precios_frutas 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450} 
Añadir las siguientes frutas con sus respectivos precios: 
● Naranja = 1200 
● Manzana = 1500 
● Pera = 2300
    
"""
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Diccionario actualizado con nuevas frutas:")
print(precios_frutas)


#Ejercicio 2
"""
Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
● Banana = 1330 
● Manzana = 1700 
● Melón = 2800
    
"""

precios_frutas = {
    'Banana': 1200, 'Ananá': 2500, 'Melón': 3000,
    'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300
}

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("Diccionario con precios actualizados:")
print(precios_frutas)

#Ejercicio 3
"""
Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
precios.
    
"""

precios_frutas = {
    'Banana': 1330, 'Ananá': 2500, 'Melón': 2800,
    'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300
}

frutas = list(precios_frutas.keys())

print("Lista de frutas:")
print(frutas)


#Ejercicio 4
"""
 Escribí un programa que permita almacenar y consultar números telefónicos. 
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
• Luego, pedí un nombre y mostrale el número asociado, si existe. 
    
"""

agenda = {}

print("Ingresá 5 contactos:")
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    telefono = input(f"Ingresá el número de {nombre}: ")
    agenda[nombre] = telefono

consulta = input("Ingresá el nombre que querés consultar: ")
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("Ese contacto no existe.")


#Ejercicio 5
"""
Solicita al usuario una frase e imprime: 
• Las palabras únicas (usando un set). 
• Un diccionario con la cantidad de veces que aparece cada palabra.
    
"""

frase = input("Ingresá una frase: ").lower()

palabras = frase.split()
palabras_unicas = set(palabras)

# Diccionario de conteo
conteo = {}
for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1

print("Palabras únicas:")
print(palabras_unicas)

print("Conteo de palabras:")
print(conteo)


#Ejercicio 6
"""
Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
Luego, mostrá el promedio de cada alumno. 
    
"""

alumnos = {}

for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    notas = tuple(float(input(f"Ingresá nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"Promedio de {nombre}: {promedio:.2f}")


#Ejercicio 7
"""
Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
y Parcial 2: 
• Mostrá los que aprobaron ambos parciales. 
• Mostrá los que aprobaron solo uno de los dos. 
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 
    
"""

parcial1 = {1, 2, 3, 4, 5}
parcial2 = {3, 4, 5, 6, 7}

ambos = parcial1 & parcial2
uno_solo = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno de los dos:", uno_solo)
print("Aprobaron al menos uno:", al_menos_uno)


#Ejercicio 8
"""
Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
Permití al usuario: 
• Consultar el stock de un producto ingresado. 
• Agregar unidades al stock si el producto ya existe. 
• Agregar un nuevo producto si no existe.
    
"""

stock = {
    "Arroz": 20,
    "Fideos": 15,
    "Harina": 10
}

producto = input("Ingresá el producto que querés consultar o actualizar: ")

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    agregar = int(input("¿Cuántas unidades querés agregar? "))
    stock[producto] += agregar
    print(f"Nuevo stock de {producto}: {stock[producto]}")
else:
    nuevo_stock = int(input(f"{producto} no existe. Ingresá stock inicial: "))
    stock[producto] = nuevo_stock
    print(f"Producto agregado. Stock de {producto}: {stock[producto]}")


#Ejercicio 9
"""
 Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
    
"""

agenda = {
    ("Lunes", "10:00"): "Reunión de equipo",
    ("Martes", "15:30"): "Llamada con cliente",
    ("Miércoles", "09:00"): "Entrenamiento"
}

dia = input("Ingresá el día: ")
hora = input("Ingresá la hora (hh:mm): ")

clave = (dia, hora)

if clave in agenda:
    print(f"Actividad en {dia} a las {hora}: {agenda[clave]}")
else:
    print("No hay actividades programadas en ese horario.")


#Ejercicio 10
"""
 Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
diccionario donde: 
• Las capitales sean las claves. 
• Los países sean los valores.
    
"""

paises = {
    "Argentina": "Buenos Aires",
    "Francia": "París",
    "Japón": "Tokio",
    "Italia": "Roma"
}

capitales = {capital: pais for pais, capital in paises.items()}

print("Diccionario invertido:")
print(capitales)

