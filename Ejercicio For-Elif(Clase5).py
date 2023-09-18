# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:59:11 2023

@author: cseba
"""

lista2 = ['r1','r2','r3','r4','s1','s2','s3','s4','AP1','fw1','OLT1']
router = []
switch = []
varios = []

for i in lista2:
    if "r" in i:
        router.append(i)
    elif 's' in i:
        switch.append(i)
    else:
        varios.append(i)
print(f'routers = {router}')
print(f'switch = {switch}')
print(f'varios = {varios}')

  
'''
### Ejemplo 
nombre = ['alison','andrea','anahi','coco','celine','erick']
letraA = []
        
for j in nombre:
    if 'a' in j:
        letraA.append(j)
print(letraA)
'''