# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 13:21:25 2026

@author: sanus
"""
from bankaccount import BankAccount

class Customer:
    def __init__(self, name: str, address: str, account: BankAccount):
        self.name= name
        self.address = address
        self.account = account
        
    def get_name(self) -> str:
        return self.name

    def get_address(self) -> str:
        return self.address

    def get_account(self) -> BankAccount:
        return self.account

    def set_name(self, name: str) -> None:
        self.name = name

    def set_address(self, address: str) -> None:
        self.address = address

    def display_info(self) -> None:
        print(f"Customer: {self.name}\nBalance: {self.account.get_balance()}")