# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 22:51:12 2026

@author: sanus
"""

import numpy as np

mark = None
mark2D = None
pass_mark = 40 
marks_1d = np.array([55, 62, 78, 95, 98, -10, 70, 88], dtype=float)
marks_2d = np.array([
    [52, 68, 75],
    [60, 72, 98],
    [45, 55, 65],
    [70, 85, 95],
    [-5, 62, 90]
], dtype=float)

def menu():
    print()
    print('====Student Data Analysis Tool====')
    print('1. Load student marks')
    print('2. View marks')
    print('3. Show statistics')
    print('4. Pass/ Fail analysis')
    print('5. Clean faulty data')
    print('6. Analyse 2D mark')
    print('7. Scale marks')
    print('8. Summary report')
    print('0. exit')

def load_data():
    global mark
    global mark2D
    mark = np.array([26,90,87,50,77,85,10,45,67,77])
    mark2D = np.array([
        [65, 70, 75],
        [80, 85, 90],
        [55, 50, 58],
        [40, 45, 50],
        [92, 88, 95],
        [48, 52, 46],
        [60, 59, 61],
        [30, 35, 40]
        ], dtype=float) # Convert to float to allow for NaN values
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

def analyse_2D_mark():
    avg_2D = np.mean(mark2D, axis=1)
    print(f"Average mark per student: {np.round(avg_2D, 2)}")
    mean_2D = np.mean(mark2D, axis=0)
    print(f"Average marks per assessment: {np.round(mean_2D, 2)}")
    fail_avg_2D = avg_2D[avg_2D < 40]
    print(f"Students with average mark below 40: {fail_avg_2D}")
    fail_ind =np.where(avg_2D < 40)[0]
    print(f"Indices of students with average mark below 40: {mark2D[fail_ind]}")

def scale_mark(mark):
    print(f"Original marks: {mark}")
    #s_cale = float(input('Enter the scale factor to apply to the marks: ')) 
    s_cale = 5
    new_mark = mark + s_cale
    clip_mark = np.clip(new_mark, 0, 100, out=new_mark) # Clip the marks to be within the range of 0 to 100
    #print(f"New marks after scaling: {np.round(new_mark, 2)}")
    #print(f"New marks after scaling and clipping: {np.round(clip_mark, 2)}")
    return clip_mark

def export_summary(mark):
    
    print("\n==============================")
    print("SUMMARY REPORT")
    print("==============================")

    if mark.ndim == 1:
        print("Data type: 1D array")
        mark[mark < 0] = np.nan  # Treat values <0 as invalid
        mark[mark > 100] = np.nan  # Treat values >100 as invalid
        mark = scale_mark(mark)
        #Complete Code
        total_students = mark.size
        overall_avg = np.nanmean(mark)
        pass_count = np.nansum(mark >= pass_mark)
        pass_rate = (pass_count / total_students * 100) if total_students > 0 else 0
        best_idx = np.nanargmax(mark)
        worst_idx = np.nanargmin(mark)

        print(pass_count)
        print(pass_rate)
        print("Scaled & clipped marks:", mark)
        print("Total students:", total_students)
        print("Overall average:", round(overall_avg, 2))
        print(f"Pass rate (%): {np.round(pass_rate, 2)}")
        print(f"Best-performing assessment: Assessment {best_idx + 1}")
        print(f"Worst-performing assessment: Assessment {worst_idx + 1}")

    elif mark.ndim == 2:
        print("Data type: 2D array")
        mark[mark < 0] = np.nan  # Treat values <0 as invalid
        mark[mark > 100] = np.nan  # Treat values >100 as invalid
        mark = scale_mark(mark)
        #Complete Code
        total_students = mark.shape[0]
        overall_avg = np.nanmean(mark, axis=1)
        ass_avg = np.nanmean(mark, axis=0)
        pass_count = np.sum(overall_avg >= pass_mark)
        pass_rate = (pass_count / total_students * 100) if total_students > 0 else 0
        best_idx = np.nanargmax(mark)
        worst_idx = np.nanargmin(mark)
        print(pass_count)
        print(pass_rate)

        print("Scaled & clipped marks:\n", mark)
        print("Total students:", total_students)
        print(f"Overall average: {np.round(overall_avg, 2)}")
        print(f"Pass rate (%): {np.round(pass_rate, 2)}")
        print(f"Best-performing assessment: Assessment {best_idx + 1}")
        print(f"Worst-performing assessment: Assessment {worst_idx + 1}")

    else:
        print("Unsupported array type")

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
    elif choice == '6':
        analyse_2D_mark()
    elif choice == '7':
        scale_mark(mark)  
    elif choice == '8':
        export_summary(marks_1d)
        export_summary(marks_2d)  
export_summary(marks_1d)
export_summary(marks_2d)  

        