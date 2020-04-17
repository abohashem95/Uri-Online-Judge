# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 13:44:06 2020

@author: abohashem
"""

def area():
    
    a,b,c = map(float, input().split())
    pi = 3.14159
    
        
    trangle = 0.5 * a * c

    circle = pi * (c**2)
    
    trapezium = ((a + b)/2) * c
    
    square = b * b
    
    rectangle = a * b 

    
    
    print ("TRIANGULO: {:.3f}".format(trangle))
    
    print("CIRCULO: {:.3f}".format(circle))
    
    print("TRAPEZIO: {:.3f}".format(trapezium))
    
    print("QUADRADO: {:.3f}".format(square))
    
    print("RETANGULO: {:.3f}".format(rectangle))
    
    



area()