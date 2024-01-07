#!/usr/bin/env python
# coding: utf-8

# In[17]:


import sympy as sy


# In[26]:


t1,t2,t3,l1,l2,l3=symbols("T1, T2, T3, L1, L2, L3")
x_dot = sy.symbols("X dot")
y_dot = sy.symbols("Y dot")
p_dot = sy.symbols("phi dot")


# In[27]:


R1 = [-l1*sin(t1)-l2*sin(t1+t2)-l3*sin(t1+t2+t3), -l2*sin(t1+t2)-l3*sin(t1+t2+t3), -l3*sin(t1+t2+t3)]
R2 = [l1*cos(t1)+l2*cos(t1+t2)+l3*cos(t1+t2+t3), l2*cos(t1+t2)+l3*cos(t1+t2+t3), l3*cos(t1+t2+t3)]
R3 = [1, 1, 1]
J=Matrix([R1, R2, R3])
J


# In[28]:


X = Matrix([x_dot, y_dot, p_dot])
X


# In[29]:


Jac_in = J.inv()
Jac_in


# In[ ]:





# In[ ]:




