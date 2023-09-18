# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 18:43:44 2023

@author: cseba
"""
### Entrada de datos 
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = int(input('Ingrese su edad: '))

### Elif 

if edad >= 1 and edad<12:
    print(f'{nombre} {apellido} de {edad} años, usted es un niño (no tiene edad para votar)')
    
elif edad >= 12 and edad<18:
    print(f'{nombre} {apellido} de {edad} años, usted es adolecente(su voto es opcional) ')

elif edad >= 18 and edad<65:
    print(f'{nombre} {apellido} de {edad} años, usted es mayor de edad(su voto es obligatorio)')
    
elif edad >=65:
    print(f'{nombre} {apellido} de {edad} años, usted es un adulto mayor(su voto es opcional)')
else:
    print('Datos incorrectos')
    

    