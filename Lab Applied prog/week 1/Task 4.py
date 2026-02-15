# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 19:58:15 2026

@author: sanus
"""

print('Sales report')
yr = int(input('Input the year the sales report is for> '))
mth1 = int(input("Input January's sales amount> "))
mth2 = int(input("Input February's sales amount> "))
mth3 = int(input("Input March's sales amount> "))
mth4 = int(input("Input April's sales amount> "))
mth5 = int(input("Input May's sales amount> "))
mth6 = int(input("Input June's sales amount> "))
mth7 = int(input("Input July's sales amount> "))
mth8 = int(input("Input August's sales amount> "))
mth9 = int(input("Input September's sales amount> "))
mth10 = int(input("Input October's sales amount> "))
mth11 = int(input("Input November's sales amount> "))
mth12 = int(input("Input December's sales amount> "))
t_tal_sal = mth1 + mth2 + mth3 + mth4 + mth5 + mth6 + mth7 + mth8 + mth9 + mth10 + mth11 + mth12
print(f"The total sales for {yr}, are £{t_tal_sal:.2f}")
