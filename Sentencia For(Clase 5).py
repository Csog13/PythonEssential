# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:19:29 2023

@author: cseba
"""

lista1 = [1,2,3,4,5,6,7]

print(len(lista1))  # Imprime la longitud de la lista
print(lista1)       # Imprime la lista


for i in lista1:
    print(i)       # Imprime cada uno de los valores
print('\n')  
 
for i in lista1:
    print(i, end=' ')    # Imprimer los valores en la misma linea separados por un espacio
print('\n')   
    
for j in range(8):       # Imprimer los valores hasta el numero 8
    print(j)      
print('\n') 
    
for a in range(2,6):     # Imprime los valores desde el 2 hasta el  6
    print(a)
print('\n') 

for b in range(2,8,2):  # Imprimer los valores del 2 hasta el 8 con pasos de 2
    print(b)