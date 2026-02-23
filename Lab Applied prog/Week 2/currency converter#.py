# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 12:40:51 2026

@author: sanus
"""

class CurrencyConverter:
    def __init__(self):
        self.__exchange_rate = 0.0
        
    def set_exchange_rate(self, rate):
        self.__exchange_rate = rate
        
    def convert_to_currency(self, amount: float):
        return amount * self.__exchange_rate
    
    def convert_from_currency(self, amount: float):
        return amount // self.__exchange_rate
    
def main():
    cc = CurrencyConverter()
    i = float(input("Enter the conversion rate"))
    cc.set_exchange_rate(i)
    v = float(input("Enter the amount: "))
    val = cc.convert_to_currency(v)
    var = cc.convert_from_currency(v)
    print("converted amount : ", val, "rate: ",var)
    
main()