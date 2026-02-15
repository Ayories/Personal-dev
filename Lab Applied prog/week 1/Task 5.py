# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 23:10:58 2026

@author: sanus
"""

import random
#random module is imported because python has no default random function

n = random.randrange(1,10)
try:
    usr_n = int(input('Input a number between 1 and 10> '))
except ValueError:
        n1 = int(input('Number only !!Input a number between 1 and 10> '))
except TypeError:
        n1 = int(input('Number only !!Input a number between 1 and 10> '))
if n == usr_n:
    print(f'Congratulation {n} is right answer')
elif n > usr_n:
    print('Guess is less than answer')
elif n < usr_n:
    print('Guess is grater than answer')
