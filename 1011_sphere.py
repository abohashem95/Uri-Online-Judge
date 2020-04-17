# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 13:30:05 2020

@author: abohashem
"""


def sphere():
    pi = 3.14159
    
    r = float(input())
    
    volume = (4/3) * pi * (r**3)
    
    print("VOLUME = {:.3f}".format(volume))
    
    
sphere()
    