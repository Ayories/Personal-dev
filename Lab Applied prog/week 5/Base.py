# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 11:11:30 2026

@author: sanus
"""

class person:
    def__init__(self, name: str, address: st)

class BankAccount:
    def __init__(self, bal: float, accNumber: int):
        self.__bal = bal
        self.__accNumber = accNumber
        
    def get_account(self, accNumber):
        return self.__accNumber
    
    def get_balance(self, bal = float):
        return self.__bal
    
    def deposit(self,amount: float):
        if amount > 0:
            self.__bal += amount
        else:
            print('Invalid Amount')