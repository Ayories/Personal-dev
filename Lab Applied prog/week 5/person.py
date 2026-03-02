# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 11:11:30 2026

@author: sanus
"""

class Person:
    def __init__(self, name: str, address: str):
        self.__name = name
        self.__address = address
    def get__name(self):
        return self.__name
    def get__address(self):
        return self.__address
    def __str__(self):
        return (
            f"name: {self.__name}\n"
            f"address: {self.__address}\n"
            )