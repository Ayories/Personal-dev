# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 23:00:33 2026

@author: sanus
"""

class BMI:
    def __init__(self):
        self.__weight = 0.0
        self.__height = 0.0

    def set_weight(self, w):
        self.__weight = w

    def set_height(self, h):
        self.__height = h

    def __cal_BMI(self):
        # BMI = weight / (height / 100)^2
        return self.__weight / ((self.__height / 100) ** 2)

    def display_BMI(self):
        bmi = self.__cal_BMI()
        print(f"BMI is {bmi:.2f}.")