# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 13:21:24 2026

@author: sanus
"""

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
    
    def withdraw(self,amount: float) :
        if amount > 0 and self.__bal >= amount:
            self.__bal -= amount
        else:
            print('Error: Insufficient funds')
        
    def transfer(self, amount, target):
        if amount > 0 and self.__bal >= amount:
            self.withdraw(amount)
            target.deposit(amount)
    
        
        
        