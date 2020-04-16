# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 00:25:09 2020

@author: abohashem
"""
def salary_1008():
    
    number = int(input())
    w_hours = int(input())
    amount_per_hours = float(input())

    salary = w_hours * amount_per_hours 
    
    print("NUMBER = {:d}".format(number))
    print("SALARY = U$ {:.2f}".format(salary))

salary_1008()