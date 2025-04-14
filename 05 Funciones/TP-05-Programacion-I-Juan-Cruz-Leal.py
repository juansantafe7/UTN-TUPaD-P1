import math


#Ejercicio 1
"""
Crear una función llamada imprimir_hola_mundo que imprima por
 pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
 programa principal.
    
"""
def imprimir_hola_mundo():
    print("Hola Mundo!")
    

imprimir_hola_mundo()

#Ejercicio 2
"""
   Crear una función llamada saludar_usuario(nombre) que reciba
 como parámetro un nombre y devuelva un saludo personalizado.
 Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
volver: “Hola Marcos!”. Llamar a esta función desde el programa
 principal solicitando el nombre al usuario
    
"""
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))



#Ejercicio 3
"""
Crear una función llamada informacion_personal(nombre, apellido,
 edad, residencia) que reciba cuatro parámetros e imprima: “Soy
 [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
dir los datos al usuario y llamar a esta función con los valores in
gresados
    
"""




def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
    
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")

informacion_personal(nombre, apellido, edad, residencia)


#Ejercicio 4
"""
 Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
dio como parámetro y devuelva el área del círculo. calcular_peri
metro_circulo(radio) que reciba el radio como parámetro y devuel
va el perímetro del círculo. Solicitar el radio al usuario y llamar am
bas funciones para mostrar los resultados
    
"""
import math


def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del círculo: "))

print(f"Área: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")


#Ejercicio 5
"""
 Crear una función llamada segundos_a_horas(segundos) que reciba
 una cantidad de segundos como parámetro y devuelva la cantidad
 de horas correspondientes. Solicitar al usuario los segundos y mos
trar el resultado usando esta función
    
"""

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundos: "))

print(f"Horas: {segundos_a_horas(segundos):.2f}")



#Ejercicio 6
"""
Crear una función llamada tabla_multiplicar(numero) que reciba un
 número como parámetro y imprima la tabla de multiplicar de ese
 número del 1 al 10. Pedir al usuario el número y llamar a la fun
ción
    
"""
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
        
numero = int(input("Ingrese un número para la tabla de multiplicar: "))

tabla_multiplicar(numero)


#Ejercicio 7
"""
 Crear una función llamada operaciones_basicas(a, b) que reciba
 dos números como parámetros y devuelva una tupla con el resulta
do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
sultados de forma clara
    
"""


def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b if b != 0 else "Infinito")

a = float(input("Primer número: "))
b = float(input("Segundo número: "))

suma, resta, multi, division = operaciones_basicas(a, b)
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multi}, División: {division}")


#Ejercicio 8
"""
Crear una función llamada calcular_imc(peso, altura) que reciba el
 peso en kilogramos y la altura en metros, y devuelva el índice de
 masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
ción para mostrar el resultado con dos decimales
    
"""

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso (kg): "))
altura = float(input("Ingrese su altura (m): "))

print(f"IMC: {calcular_imc(peso, altura):.2f}")


#Ejercicio 9
"""
Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
 una temperatura en grados Celsius y devuelva su equivalente en
 Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
 resultado usando la función
    
"""

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Temperatura en °C: "))

print(f"Temperatura en Fahrenheit: {celsius_a_fahrenheit(celsius):.2f}")


#Ejercicio 10
"""
Crear una función llamada calcular_promedio(a, b, c) que reciba
 tres números como parámetros y devuelva el promedio de ellos.
 Solicitar los números al usuario y mostrar el resultado usando esta
 función
    
"""



def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Primer número: "))
b = float(input("Segundo número: "))
c = float(input("Tercer número: "))

resultado = calcular_promedio(a, b, c)
print(f"Promedio: {resultado:.2f}")




