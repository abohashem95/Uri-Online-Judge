# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 21:20:10 2020

@author: abohashem
"""

def Greatest():
    
    a, b, c = map(int,input().split())
    
    
    maior_ab = (a+b+abs(a-b))/2
    maior_abc = (maior_ab+c+abs(maior_ab-c))/2
    
    print(int(maior_abc),"eh o maior")
    
    
    
    
    
    
Greatest()