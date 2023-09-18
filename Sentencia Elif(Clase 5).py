"""
Created on Tue Sep 12 18:43:44 2023

@author: cseba
"""

acl = int(input('Ingrese el dato del numero de ACL: '))


if acl >= 1 and acl <= 99:
    print('El ACL es estandar')

elif acl >= 100 and acl <= 199:
    print('Es un ACL extendida')
    
else:
    print('El valor ingresado no es un ACL')