# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 22:47:10 2026

@author: sanus
"""

from bankaccount import BankAccount
from customer import Customer

def main():
    # 1 & 2. Create bank accounts and link them to new customers 
    account1 = BankAccount(1, 0.0)
    customer1 = Customer("Ali", "Birmingham", account1)
    
    account2 = BankAccount(2, 0.0)
    customer2 = Customer("Sara", "Coventry", account2)

    # 3. Create a list of the two customers [cite: 150]
    customers = [customer1, customer2]

    # a) Deposit 100 into each customer's account 
    for c in customers:
        c.get_account().deposit(100)

    # b) Withdraw 40 from each account 
    for c in customers:
        c.get_account().withdraw(40)

    # c) Display balances for all customers 
    print("--- After initial deposit and withdrawal ---")
    for c in customers:
        c.display_info()
        print("-" * 20)

    # d) Deposit 20 into each account 
    for c in customers:
        c.get_account().deposit(20)

    # e) Display balances again 
    print("\n--- After second deposit ---")
    for c in customers:
        c.display_info()
        print("-" * 20)

    # f) Transfer 20 from the second customer's account to the first customer's account 
    customer2.get_account().transfer(20, customer1.get_account())

    # g) Display final balances 
    print("\n--- Final Balances ---")
    for c in customers:
        c.display_info()
        print("-" * 20)

if __name__ == "__main__":
    main()