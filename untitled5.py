# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:56:55 2023

@author: Vanesa
"""

lista=['R1','R2','R3',
       's1','s2','S3']
print(len(lista))
'''
print (lista[0])
print (lista[S])
'''
for item in lista:
    if 'R' in item:
        print(item,end=' * ')