# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 20:24:56 2023

@author: cseba
"""

### While
'''
numero = int(input('Ingrese el numero al que debo contar: '))
contador = 1

while contador <= numero :
    print(contador)
    contador = contador + 1
 ''' 
    
'''
### Break (Se usa detener el codigo)
numero = int(input('Ingrese el numero al que debo contar: '))
contador = 1

while True :
    print(contador)
    contador = contador + 1
    if contador > numero:
        break

'''

while True:
    x = input('Enter a number to count to: ')
    if x == 'q' or x =='quit':
      break


    x = int(x)
    y = 1 

    while True:
      print(y)
      y = y + 1 
      if y > x:
        break 