# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 18:36:47 2023

@author: cseba
"""

### Funciones 
'''
def Mensaje ():                # Definicon de una funcion 
    print('Ingrese un dato')
    
Mensaje()                      # Invocacion de la funcion 
'''
###### Funcion con variables

def saludo(nombre):            # Argumento(nombre) necesario en la funcion 
    print(f'Hola {nombre}')
    
# saludo('Sebas')

def FechasCum(dia,mes):
    print(f'Su fecha de cumple años el dia: {dia}, mes: {mes}')

# DiaCum = int(input("Ingrese su dia de cumpleanos: "))
# MesCum = input('Ingrese su mes de cumpleanos: ')

# FechasCum(DiaCum, MesCum)

def direct(ciudad,barrio,calle):
    print(f'La ciudad de entrega es : {ciudad} ')
    print(f'El sector es: {barrio}')
    print(f'El pedido esta en la calle: {calle}')
    
# ba = input('Ingrese el barrio: ')
# ci = input('Ingrese la ciudad: ')
# cl = input('Ingrese la calle: ')

# direct(ci, ba, cl)

def ID(nombre,apellido,cedu):
    print('-----------------------')
    print(f'Ciudadano de nombre: {nombre} {apellido}')
    print(f'C.I: {cedu}')
    print('-----------------------')
    
# nom = input('Ingrese su nombre: ')
# apel = input('Ingrese si apellido: ')
# ci = int(input('Ingrese su cedula de identidad: '))

# ID(nom,apel,ci)

##================Formas de pasar argumentos============== 
'''
def res(a,b):
    resultado = a - b
    print(resultado)
    
res(a = 4,b = 5)
res(b = 8,a = 2)
res(5,b = 2)
# res(a = 6,5) no se puede pasar valores de esta forma
'''
#===============Return===================================
'''
def resta(a,b):
    print(a - b)
    return (a - b)
    
# x = resta(5,1)
# opt = x + 1 
# print(opt)

def suma(a, b, c):
    resultado = a + b + c
    return resultado

ResuSum = suma(5, 4, 6)
promedio = ResuSum / 5
print(promedio)


def saludo3(lista):
    for i in lista:
        print(f'Hola ,{i}')
    print('')

saludo3(['Juan','Erick'])


def crealista(n):
    lista = []
    for i in range(n):
        lista.append(i)
    return lista

print(crealista(10))

### Funcion Ejercicio Numerpp Primo 
def EsPrimo (num):
    #if num < 2:
    #   return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True


for i in range(1, 20):
	if EsPrimo (i + 1):
			print(i + 1, end=" ")
print()

'''
 #### ========Funciones Lamda===========
 


