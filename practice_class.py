#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:21:09 2017

@author: atlas
"""

class Line(object):
    def __init__(self, coord1, coord2):
        self.coord1=coord1
        self.coord2=coord2
        
    def distance(self):
        return np.linalg.norm(np.array(coord1)-np.array(coord2))
    
    def slope(self):
        return (coord1[1]-coord2[0])/(coord1[0]-coord2[0])

class Circle(object):
    def __init__(self, radius):
        self.radius=radius
        
    def area(self):
        return np.pi*self.radius**2
    
    def perimeter(self):
        return 2*np.pi*self.radius



    
import numpy as np
coord1=(3,2)
coord2=(8,10)

li=Line(coord1, coord2)

print(li.slope())
print(li.distance())

radius=10

ci=Circle(radius)

print("The area is : ", ci.area())
print("The Perimeter is : ", ci.perimeter())
