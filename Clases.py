# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 18:36:57 2023

@author: cseba
"""
############### CLASE ##############

## Creacion de clase
class MiPrimeraClase:
    pass

#Creacion de objetos con la clase
obj1 = MiPrimeraClase()
obj2 = MiPrimeraClase()
obj3 = MiPrimeraClase()



class Empleado:
    #contador
    contadoremp = 0 
    def __init__(self,name,surname):
        self.name = name 
        self.surname = surname
        Empleado.contadoremp += 1
        
    