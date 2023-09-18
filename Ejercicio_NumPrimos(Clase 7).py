# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 17:41:57 2023

@author: cseba
"""

def EsPrimo (num):
    
    for i in range(2,num):
        if num % i == 0:
            return False
    return True


for i in range(1, 20):
	if EsPrimo (i + 1):
			print(i + 1, end=" ")
print()
