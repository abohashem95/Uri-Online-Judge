# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 00:44:35 2020

@author: abohashem
"""

def salary_with_bonus():
    name = str(input())
    salary = float(input())
    sold_value = float(input())
    
        
    bonus = (sold_value * 15)/100        
    total_payment = bonus + salary
    print("TOTAL = R$ {:.2f}".format(total_payment))

    
salary_with_bonus()