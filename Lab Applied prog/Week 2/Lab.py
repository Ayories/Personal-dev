# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 22:51:12 2026

@author: sanus
"""

import numpy as np

mark = None
mark2D = None

def menu():
    print()
    print('====Student Data Analysis Tool====')
    print('1. Load student marks')
    print('2. View marks')
    print('3. Show statistics')
    print('4. Pass/ Fail analysis')
    print('5. Clean faulty data')
    print('6. Analyse 2D mark')
    print('0. exit')

def load_data():
    global mark
    global mark2D
    mark = np.array([26,90,87,50,77,85,10,45,67,77])
    mark2D = np.array([
        [26,90],
        [87,50],
        [77,85],
        [10,45],
        [67,77]
        ])
    print(mark)
    print('Data Type: ',mark.dtype) #the .dtype shows the data type of the elements in the array
    print('Number of students: ',mark.size) #the .size shows the number of the elements in the array
    print(f""" The marks of students are {mark}, there are {mark.size} of them and they are of {mark.dtype} datatype """)

def view_data():
    print('All student Marks')
    print('First Mark: ', mark[0])
    print('Last Mark: ', mark[-1])    
    n = mark.size // 2
    print('Centre(middle) 3 marks are ', mark[n - 1:n + 2])
    print(mark2D)
def show_data():
    global m_an
    global m_ax
    global m_in
    global m_std
    m_an = np.mean(mark)
    m_ax = np.max(mark)
    m_in = np.min(mark)
    m_std = np.std(mark)
    print(f"Mean mark is {m_an:.2f}")
    print(f"Max mark is {m_ax:.2f}")
    print(f"Min mark is  {m_in:.2f}")
    print(f"'STD is {m_std:.2f}")
    if m_an < 40:
        print('The average marks suggest the overall marks are unsatisfactory.')
    else:
        print('The average marks suggest the overall marks are satisfactory.')
    
def data_analyse():
    pass_mark = mark[mark >= 40]
    fail_mark = mark[mark < 40]
    total_mark = mark.size
    pass_perc = (float(pass_mark.size) / total_mark) * 100
    print('The passed marks are ',pass_mark)
    print('The failed marks are ',fail_mark)
    print('The number of passed marks are ', pass_mark.size)
    print('The number of failed marks are ',fail_mark.size)
    print(f"The pass percentage is {pass_perc:.2f}%")
    if pass_perc >= 80:
        print('Excellent pass rate overall')
    elif pass_perc >= 60 and pass_perc <= 80:
        print('Pass rate is satisfactory overall.')
    elif pass_perc >= 50 and pass_perc <= 60:
        print('Pass rate is good, may require improvement.')
    elif pass_perc < 50:
        print('Pass rate is low, Additional Support Required.')

def clean_data():  
    mark = np.array([44, -30, 90, 80, 33, -60, 101, 55], dtype=float) # Convert to float to allow for NaN values
    invalid_count = (mark < 0) | (mark > 100)
    removed_count = np.sum(invalid_count)
    mark[invalid_count] = np.nan  # Replace invalid marks with NaN
    print(invalid_count)
    print(f"Cleaned data: {mark}")    
    print(f"Updated mean (ignoring NaN): {np.nanmean(mark):.2f}")
    print(f"Number of removed marks: {removed_count}")
while True:
    menu()
    choice = input('Select an option: ')
    
    if choice == '0':
        print ('Exiting Program ..')
        break
    elif choice == '1':
        load_data()
    elif choice == '2':
        view_data()
    elif choice == '3':
        show_data()
    elif choice == '4':
        data_analyse()
    elif choice == "5":
        clean_data()
        