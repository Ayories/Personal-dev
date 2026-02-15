# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print('Mark calculator')
m1 = float(input('Input the first mark> '))
w1 = float(input('Input the weight of the first mark> '))
m2 = float(input('Input the second mark> '))
w2 = float(input('Input the weight of the second mark> '))
m3 = float(input('Input the third mark> '))
w3 = float(input('Input the weight of the third mark> '))
w11 = m1 * w1/100
w21 = m2 * w2/100
w31 = m3 * w3/100
o_w = w11 + w21 + w31
print('The overal mark for the marks and weighted input is')
print('Mark1 = ' ,m1 ,'Weight1 = ' ,w1 ,'% weighted mark = ' ,m1 ,'*' ,w1 ,'% = ' ,w11)
print('Mark2 = ' ,m2 ,'Weight2 = ' ,w2 ,'% weighted mark = ' ,m2 ,'*' ,w2 ,'% = ' ,w21)
print('Mark3 = ' ,m3 ,'Weight1 = ' ,w3 ,'% weighted mark = ' ,m3 ,'*' ,w3 ,'% = ' ,w31)

print('Overall mark is ' ,w11 ,'% + ' , w21 ,'% + ' , w31 ,'% = ' ,o_w ,'%')