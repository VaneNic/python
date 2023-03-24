# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 18:34:30 2023

@author: Vanesa
"""

Firstname=input('Nombre: ')
lastname=input('Apellido: ')
Location= input('Sector: ')
Age=int(input('Edad: '))
if Age >=0 and Age <=5:
    print('Primera Infancia')
elif Age >=6 and Age <=11:
    print('Infancia')
elif Age >=12 and Age <=18:
    print('Adolescencia')
elif Age >=18 and Age <=26:
    print('Juventud')
elif Age >=27 and Age <=59:
    print('Adultez')
elif Age >=60:
    print ('persona Mayor')
space= ""
print('Estimado/a',Firstname,lastname,'con la edad ',Age, 'años usted pueder ser partícipe de la campaña NEW TECHNOLOGY en el sector de', Location)
