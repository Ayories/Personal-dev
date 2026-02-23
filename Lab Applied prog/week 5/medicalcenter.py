# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 12:08:14 2026

@author: luxex
"""
class MedicalCenter:
    def __init__(self, c_name: str, c_address: str, ):
        self.__c_name = c_name
        self.__c_address = c_address
        
    def get_c_name(self):
        return self.__c_name
    
    def get_c_address(self):
        return self.__c_address
    
    def __str__(self):
        return (
            "Medical Center\n"
            f"c_name: {self.__c_name}\n"
            f"c_address: {self.__c_address}"
            )
        
