# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 20:02:09 2023

@author: cseba
"""

### Ingreso de datos 
print('------------------------------Informacion del cliente-----------------------------------')
nombre = input('Ingrese el nombre del cliente : ')
apellido = input('Ingrese el apellido del cliente: ')
edad = int(input('Ingrese la edad del cliente: '))
direccion = input('Ingrese la direccion del cliente: ')

### Pantalla

print('----------------------------------Impresion de Orden-----------------------------------')
print(f'El cliente de nombre {nombre} {apellido} de {edad} años,tiene una deuda con el estado la cual sera pasada a cancelar al domicilio de direccion {direccion}')


