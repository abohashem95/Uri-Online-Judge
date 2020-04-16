# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 18:57:05 2020

@author: abohashem
"""

def simple_calculate():
    
    product1_num,unit1_num,unit1_price = map(float,input().split())
    product2_num,unit2_num,unit2_price = map(float,input().split())
    
    value_to_pay = (unit1_num * unit1_price) + (unit2_num * unit2_price)
    
    print("VALOR A PAGAR: R$ {:.2f}".format(value_to_pay))
    
    
simple_calculate()