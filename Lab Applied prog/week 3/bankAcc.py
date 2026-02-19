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
    
    def get_balance(self, bal):
        return self.get_balance(bal)
    
    def deposit(self,amount):
        if amount > 0:
            self.__bal += amount
        else:
            print('Invalid Amount')
    
    def withdraw(self,amount):
        if self.__bal >= amount:
            self.bal -= amount
        else:
            print('Error: Insufficient funds')
        
    def transfer(self, amount, target):
        self.withdraw(amount)
        self.deposit(amount)
        
        
        