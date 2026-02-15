# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 00:07:06 2026

@author: sanus
"""

print('Ascending order')
try:
    n1 = int(input('Input the first number> '))
except ValueError:
        n1 = int(input('Number only !!Input the first number> '))
except TypeError:
        n1 = int(input('Number only !!Input the first number> '))
try:
    n2 = int(input('Input the second number> '))
except ValueError:
       n2 = int(input('Number only !!Input the second number> '))
except TypeError:
       n2 = int(input('Number only !!Input the second number> '))
if n1 > n2 : 
    print('Numbers were swapped')
    print(" First number is %d" %n2 )
    print(" Second number is %d" %n1 )
elif n2 > n1:
    print(" First number is %d" %n1 )
    print(" Second number is %d" %n2)
