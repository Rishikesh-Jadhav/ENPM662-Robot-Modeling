#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import sympy as sp
import math as m
from sympy.matrices import Matrix
from numpy import cos,sin


# In[6]:


x, y, z = sp.symbols("x, y, z") 

def inputs():
    trans_x = float(input("Enter transition in X :"))       
    trans_y = float(input("Enter transition in Y : "))      
    trans_z = float(input("Enter transition in Z : ")) 
    
    print("Angles is degrees") 
    rot_x = float(input("Enter psi  : "))     # along x_axis
    rot_y = float(input("Enter theta  : "))   # along y_axis  
    rot_z = float(input("Enter phi  : "))     # along z_axis  
#     Converting from degrees to radians 
    psi = np.radians(rot_x)
    theta = np.radians(rot_y)                       
    phi = np.radians(rot_z)  
 
    
    return trans_x,trans_y,trans_z,theta,phi,psi

def calculate_values(dx,dy,dz,theta,phi,psi): 

    eqn = y*cos(phi)*sin(psi) + y**2*cos(phi)**2*cos(psi)**2 - x*sin(phi)*sin(psi) + x**2*cos(phi)**2*cos(theta)**2 + y**2*sin(phi)**2*sin(psi)**2*sin(theta)**2 - x**2*cos(psi)*cos(theta)*sin(phi)**2 - y**2*cos(psi)*cos(theta)*sin(phi)**2 - x*cos(phi)*cos(psi)*sin(theta) - y*cos(psi)*sin(phi)*sin(theta) + dy*y*cos(phi)*cos(psi) + dx*x*cos(phi)*cos(theta) - dy*x*cos(psi)*sin(phi) + dx*y*cos(theta)*sin(phi) - x*y*cos(phi)*cos(psi)**2*sin(phi) + x*y*cos(phi)*cos(theta)**2*sin(phi) + dy*x*cos(phi)*sin(psi)*sin(theta) + dy*y*sin(phi)*sin(psi)*sin(theta) + x*y*cos(phi)**2*cos(psi)*sin(psi)*sin(theta) + x*y*cos(phi)**2*cos(theta)*sin(psi)*sin(theta) - x*y*cos(psi)*sin(phi)**2*sin(psi)*sin(theta) + x*y*cos(theta)*sin(phi)**2*sin(psi)*sin(theta) + 2*y**2*cos(phi)*cos(psi)*sin(phi)*sin(psi)*sin(theta) + x**2*cos(phi)*cos(theta)*sin(phi)*sin(psi)*sin(theta) + x*y*cos(phi)*sin(phi)*sin(psi)**2*sin(theta)**2 + y**2*cos(phi)*cos(theta)*sin(phi)*sin(psi)*sin(theta)
    a = eqn.coeff(x, 2)                                 #coefficient of x^2
    b = eqn.coeff(x*y, 1)/2                             #coefficient of xy/2                          
    c = eqn.coeff(y, 2)                                 #coefficient of y^2                        
    d = eqn.coeff(x, 1)/2 - y*eqn.coeff(x*y, 1)/2        
    e = eqn.coeff(y, 1)/2 - x*eqn.coeff(x*y, 1)/2       
    f = eqn - a*x**2 - b*x*y*2 - c*y**2 - d*x*2 - e*y*2 
    
    coef_matrix = Matrix([[a, b, d], [b, c, e], [d, e, f]]) 
    matrix_det = coef_matrix.det()
    
    
    area = -m.pi*matrix_det/(a*c - b**2)**(3/2)         #Area formula     
    return area

def print_area(area):
    print("Area of the Ellipse is :",area)

# Calling all functions to get desired outputs based on the user inputs

dx,dy,dz,theta,phi,psi=inputs()
area=calculate_values(dx,dy,dz,theta,phi,psi)
print_area(area)


# In[ ]:





# In[ ]:




