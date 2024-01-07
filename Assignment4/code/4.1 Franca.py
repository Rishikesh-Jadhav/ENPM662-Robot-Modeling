from sympy import * 
from sympy.matrices import Matrix
from sympy import pprint
import numpy as np
import matplotlib.pyplot as plt

#Function to create a Transformation matrix using DH parameters - α, θ, d, a
def Transformation_matrix(alpha, theta, d, a):
    #Converting to float
    d = float(d)            
    a = float(a)
    #Transformation matrix 'T'
    
    T = Matrix([[cos(theta), -sin(theta)*cos(alpha), sin(theta)*sin(alpha), a*cos(theta)], 
    [sin(theta), cos(theta)*cos(alpha), -cos(theta)*sin(alpha), a*sin(theta)], 
    [0, sin(alpha), cos(alpha), d], 
    [0, 0, 0, 1]])
    return T


theta = np.linspace(90, 450, num=50)  
 #dt = T/N where T = 5 sec and N = 50
dt = 5/50  
x = []
y = []
z = []


q1_1 = Symbol('Theta1')
q2_1 = Symbol('Theta2')
q3_1 = Symbol('Theta4')
q4_1 = Symbol('Theta5')
q5_1 = Symbol('Theta6')
q6_1 = Symbol('Theta7')

#Setting Initial Joint angles
q1 = 0     
q2 = 0     
q3 = pi/2  
q4 = 0     
q5 = pi    
q6 = 0 

 #Creating homogeneous Transformation matrices 

T1 = Transformation_matrix(pi/2,q1_1,0.333,0)       
T2 = Transformation_matrix(-pi/2,q2_1,0,0)           
T3 = Transformation_matrix(-pi/2,0,0.3160,0.088)     
T4 = Transformation_matrix(pi/2,q3_1,0,-0.088)       
T5 = Transformation_matrix(pi/2,q4_1,0.3840,0)       
T6 = Transformation_matrix(-pi/2,q5_1,0,0.088)        
T7 = Transformation_matrix(0,q6_1,-0.207,0)          
H1 = T1
H2 = H1*T2
H3 = H2*T3*T4
H4 = H3*T5
H5 = H4*T6
H6 = H5*T7

# Z component of frames

Z0 = Matrix([[0], [0], [1]])                
Z1 = Matrix([[H1[2]], [H1[6]], [H1[10]]])   
Z2 = Matrix([[H2[2]], [H2[6]], [H2[10]]])   
Z3 = Matrix([[H3[2]], [H3[6]], [H3[10]]])   
Z4 = Matrix([[H4[2]], [H4[6]], [H4[10]]])   
Z5 = Matrix([[H5[2]], [H5[6]], [H5[10]]])   
Z6 = Matrix([[H6[2]], [H6[6]], [H6[10]]])   

#Translation of final transformation matrix - H6

Xp = Matrix([[H6[3]], [H6[7]], [H6[11]]])   

#Differentitaing Xp w.r.t all thetas

C1 = diff(Xp, q1_1) 
C2 = diff(Xp, q2_1) 
C3 = diff(Xp, q3_1) 
C4 = diff(Xp, q4_1) 
C5 = diff(Xp, q5_1) 
C6 = diff(Xp, q6_1) 

#Computing Jacobians for all columns

J1 = Matrix([[C1], [Z1]]) 
J2 = Matrix([[C2], [Z2]]) 
J3 = Matrix([[C3], [Z3]]) 
J4 = Matrix([[C4], [Z4]]) 
J5 = Matrix([[C5], [Z5]]) 
J6 = Matrix([[C6], [Z6]]) 

J = Matrix([[J1, J2, J3, J4, J5, J6]])
pprint(J)
    

fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111, projection='3d')

for t in theta:

    # X-Y-Z components of velocity

    Vx = 0                               
    Vy = -0.1*2*(pi/5)*sin(t*(pi/180))  
    Vz = 0.1*2*(pi/5)*cos(t*(pi/180))   
    Wx = 0     

    # Angular velocities

    Wy = 0
    Wz = 0

    # Velocity matrix
    x_dot = Matrix([[Vx], [Vy], [Vz], [Wx], [Wy], [Wz]]) 
    J_1 = J.evalf(subs ={q1_1 : q1, q2_1 : q2, q3_1 : q3, q4_1 : q4, q5_1 : q5, q6_1 : q6}) # Substituting theta values in Jacobian Matrix
    H6_1 = H6.subs({q1_1 : q1, q2_1 : q2, q3_1 : q3, q4_1 : q4, q5_1 : q5, q6_1 : q6})      # Substituting theta values in Final Trasnformation Matrix H6
    
    # X-Y-Z components of end effector position
    # Appending these values to the respective lists to be able to plot them when the loop runs

    x.append(H6_1[3])   
    y.append(H6_1[7])   
    z.append(H6_1[11])  
    ax.scatter(H6_1[3], H6_1[7],H6_1[11])
    plt.xlim(0, 1)
    plt.ylim(-0.15, 0.15)
    ax.set_xlabel('X', fontweight ='bold')
    ax.set_ylabel('Y', fontweight ='bold')
    ax.set_zlabel('Z', fontweight ='bold')
    ax.set_title('Trajectory plotting of the end effector', fontsize = 16, fontweight ='bold')
    plt.pause(0.5)

    # Getting the angular joint velocity Matrix
    q_dot = J_1.pinv()*x_dot    
    q1_dot = q_dot[0]
    q2_dot = q_dot[1]
    q3_dot = q_dot[2]
    q4_dot = q_dot[3]
    q5_dot = q_dot[4]
    q6_dot = q_dot[5]
 
    # Integrating the joint angular velocities to get new joint angles
    q1 = q1 + (q1_dot*dt) 
    q2 = q2 + (q2_dot*dt)
    q3 = q3 + (q3_dot*dt)
    q4 = q4 + (q4_dot*dt)
    q5 = q5 + (q5_dot*dt)
    q6 = q6 + (q6_dot*dt)
    q1 = q1.evalf()
    q2 = q2.evalf()
    q3 = q3.evalf()
    q4 = q4.evalf()
    q5 = q5.evalf()
    q6 = q6.evalf()

plt.show()