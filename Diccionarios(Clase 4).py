# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 18:51:35 2023

@author: cseba
"""

## Diccionarios 

diccionario1 = {'r1':'10.10.10.1',
                'r2':'10.10.10.2',
                'alumno':'Carlos',
                'ID':'1726195298'}

print(diccionario1)

'''Impresion del valor de la clave r1'''
print(diccionario1['r1'])

'''Agregar elementos a un diccionario'''
diccionario1['r3'] = '10.10.10.3'
print(diccionario1)

'''Modifica elementos del diccionario'''
diccionario1['r2'] = '10.10.10.2.1'
print(diccionario1)

'''Eliminar elementos de un diccionario'''
del(diccionario1['ID'])
print(diccionario1)
