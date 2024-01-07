#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import math
import random 
import matplotlib.pyplot as plt


# In[45]:


pi = math.pi

omega = (2*pi)/3   # Angular Acceleration
R = 0.25           # Radius
alpha = pi/6       # Steering angle
L = 4              # Length of the chassis
Us = omega*R       # Linear velocity
T = 0              # Time
dt = 0.1
theta = theta_i

x_list = []        # Creating an empty list to append data points.
y_list = []


while time <= 10000:
    x_dot = Us*math.sin(theta + alpha)
    y_dot = Us*math.cos(theta + alpha)
    theta_dot = Us*math.sin(alpha)/L
    
    x = x + x_dot*dt
    y = y + y_dot*dt
    theta = theta + theta_dot*dt
    
    
    x_list.append(x)
    y_list.append(y)
    
    T = T + dt
        
plt.plot(x_arr,y_arr,'r.-')
plt.show()
    


# In[ ]:




