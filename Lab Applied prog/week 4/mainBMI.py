# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 23:00:33 2026

@author: sanus
"""
from Lab8_BMI import BMI

def main():
    person = BMI()
    person.set_weight(65.0)  # Example weight in kg
    person.set_height(170.0) # Example height in cm
    person.display_BMI()

main()
