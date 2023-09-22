# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 18:23:31 2023

@author: cseba
"""

## Manejo de errores 

print('INICIO')
try:
    print('1')
    x = 1 / 0 
    print('2')
    
except:
    print('Hay un error')
print('3')
print('FIN')


# Ejemplo 2 
print('INICIO')
try:
    print('1')
    x = 1 / 0 
    print('2')
    
except:
    print('Hay un error')
print('3')
print('FIN')


## varios excepciones 
try:
    x = int(input('Ingrese un numero: '))
    y = 1 / x 
    print(y)

except ZeroDivisionError:
    print('You cant divide by zero, sorry.')
except ValueError:
    print('You must enter an integer  value.')
except:
    print('Oh dear, something went wrong...')
print('The end ')

## 

try:
    y = 1/0
    
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print('Arithmetic problem!')
    
print('THE END')

## Error de asercion 

import math
x=float(input("Ingrese un numero: "))
assert x>=0.0
x=math.sqrt(x)
print(x)