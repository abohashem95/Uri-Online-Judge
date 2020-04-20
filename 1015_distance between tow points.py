# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 21:27:24 2020

@author: abohashem
"""

import math

def Distance_Between_Two_Points():
    
    x1, y1 = map(float,input().split())
    x2, y2 = map(float,input().split())
        
    
    dist = math.sqrt( ((x2-x1)**2) + ((y2-y1)**2))
    
    print("{:.4f}".format(dist))
    
    
    

Distance_Between_Two_Points()    