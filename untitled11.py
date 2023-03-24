# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 18:58:52 2023

@author: Vanesa
"""

def multi(num1,num2):
    print('el resultado de multiplicar ',
          num1, ' * ', num2,
          'es: ',num1*num2, '\n')
    return num1+num2
multi(50,num2=6)
multi(85,96)
multi(num1=4,num2=89)
resultado=multi(85, 96)
opt=resultado*1.12
print(opt)