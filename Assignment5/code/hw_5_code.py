
import numpy as np
import  matplotlib.pyplot as plt
from mpmath import mp
from sympy import *
from sympy import cos as c 
from sympy import sin as s

init_printing(wrap_line=False)

def matrix_generator(theta,alpha,a,d):
    #subsituting values for Transformation matrix 

    matrix=Matrix([[c(theta),-s(theta)*c(alpha),s(theta)*s(alpha),a*c(theta)],
    [s(theta),c(theta)*c(alpha),-c(theta)*s(alpha),a*s(theta)],
    [0,s(alpha),c(alpha),d],
    [0,0,0,1]])
    return matrix

def jacobian_calculator(Z_joint,O_end,theta_derive):
    
    #calculating jcobain using second method

    Z_joint.row_del(3)
    O_end.row_del(3)       
    diff_result=diff(O_end,theta_derive)
    col_vector=diff_result.col_join(Z_joint)
    return col_vector

       
def get_coordinates(vector,x_list,y_list,z_list,coor_matrix,z):

    # if z==0:    #substituting intial value
    #     vector=Matrix([[0],[0],[mp.pi/2],[0],[mp.pi],[0]])

    result=coor_matrix.subs([(theta_1,vector[0]),(theta_2,vector[1]),(theta_3,vector[2]),(theta_4,vector[3]),(theta_5,vector[4]),(theta_6,vector[5])])
    resultant_vector=result.col(3) #converting 3x1 matrix
    x=resultant_vector[0]
    y=resultant_vector[1]
    z=resultant_vector[2]    
    x_list.append(x)
    y_list.append(y)
    z_list.append(z)
    return x_list,y_list,z_list #returning list of end efffector x,y,z values

# def cal_pe(centre_of_mass,mass,gravity):
#     p_e= mass*gravity*transformation_matrix*centre_of_mass
#     return p_e

# def cal_g_matrix(pe,q_derive):
#     pe_derivative=diff(pe,q_derive)
#     return pe_derivative



#defining variables
list=[1,2,3,4,5,6,7]
list_1=[1,2,3,4,5,6]
theta_1,theta_2,theta_3,theta_4,theta_5,theta_6,theta_d= Symbol("theta1"),Symbol("theta2"),Symbol("theta3"),Symbol("theta4"),Symbol("theta5"),Symbol("theta6"),Symbol("thetad")

# matrix_values=[[theta_1,mp.pi/2,0,0.333],[theta_2,-mp.pi/2,0,0],[0,-mp.pi/2,0.0880,0.3160],[theta_3,mp.pi/2,-0.0880,0],[theta_4,mp.pi/2,0,0.384],[theta_5,-mp.pi/2,0.0880,0],[theta_6,0,0,-0.207]]

d1, d3, d5, d7, a3 = Symbol("d1"),Symbol("d3"),Symbol("d5"),Symbol("d7"),Symbol("a3")
matrix_values=[[theta_1,mp.pi/2,0,d1],[theta_2,-mp.pi/2,0,0],[0,-mp.pi/2,a3,d3],[theta_3,mp.pi/2,-a3,0],[theta_4,mp.pi/2,0,d5],[theta_5,-mp.pi/2,a3,0],[theta_6,0,0,-d7]]
theta_list=[theta_1,theta_2,theta_3,theta_4,theta_5,theta_6]
result_matrix=[]
x_coord=[]
y_coord=[]
z_coord=[]

center_of_mass_links=Matrix([])



#getting individual matrixes 

for i in range(len(list)):
    params=matrix_values[i]
    final_matrix=matrix_generator(*params)
    result_matrix.append(final_matrix)

#calulating matrixes, joints wrt base frame

ans_1=result_matrix[0] #T0->1
ans_2=ans_1*result_matrix[1]*result_matrix[2]#T0->dummy link
ans_3=ans_2*result_matrix[3]#T0->4
ans_4=ans_3*result_matrix[4]#T0->5
ans_5=ans_4*result_matrix[5]#T0->6
ans_6=ans_5*result_matrix[6]#T0->end effector
theta_values=[0,0,pi/2,0,pi,0]
transformation_matrix=[ans_1,ans_2,ans_3,ans_4,ans_5,ans_6]

jacobian_matrix=[]

#calculating jacobian columns and merging to form matrix 

for i in range(len(list_1)):
    z_vector=transformation_matrix[i].col(2)
    o_end_vector=transformation_matrix[5].col(3)
    theta_value=theta_list[i]
    jacobian=jacobian_calculator(z_vector,o_end_vector,theta_value)
    jacobian_matrix.append(jacobian)


jacobian_matrix=Matrix([ [jacobian_matrix[0],jacobian_matrix[1],jacobian_matrix[2],jacobian_matrix[3],jacobian_matrix[4],jacobian_matrix[5]] ])
jacobian_matrix=jacobian_matrix.subs([(d1, 0.333),(d3, 0.3160),(d5,0.3840),(d7,0.2070),(a3,0.088)]).evalf()

# print(jacobian_matrix)

jacobian_matrix_1=jacobian_matrix.subs([(theta_1,0),(theta_2,0),(theta_3,pi/2),(theta_4,0),(theta_5,pi),(theta_6,0)])

#finding COM of all links 

#Assuming all links have uniform mass distribution 

com_1=ans_1.subs([(d1, d1/2)])[2,3]
com_2=ans_2.subs([(d3, d3/2), (a3, a3/2)])[2,3]
com_3=ans_4.subs([(d5,d5/2)])[2,3]
com_4=ans_5.subs([(a3, a3/2)])[2,3]
com_5=ans_6.subs([(d7, d7/2)])[2,3]
mass_1,mass_2,mass_3,mass_4,mass_5 = 4.970,3.228 + 0.6469,1.225 + 3.587,1.666,0.735

#finding potential energy of system

Potential_energy=9.8*(mass_1*com_1 + mass_2*com_2 + mass_3*com_3 + mass_4*com_4 + mass_5*com_5)
Potential_energy=Potential_energy.subs([(d1, 0.333),(d3, 0.3160),(d5,0.3840),(d7,0.2070),(a3,0.088)]).evalf()
#calculating gravity matrix

g_q=Matrix([[Potential_energy.diff(theta_list[0])],[Potential_energy.diff(theta_list[1])],[Potential_energy.diff(theta_list[2])],[Potential_energy.diff(theta_list[3])],[Potential_energy.diff(theta_list[4])],[Potential_energy.diff(theta_list[5])]])
pprint(g_q)

#defining values to find q and torque

omega=(2*mp.pi)/200
radius=0.10
time=0
x_dot=0
q=Matrix([[0],[0],[mp.pi/2],[0],[mp.pi],[0]])
points=np.linspace(0,200,50)
z=0
force=Matrix([[-5],[0],[0],[0],[0],[0]])
torque_values=[]

#defining graph

ax = plt.axes(projection='3d')
ax.set_xlim(0, 1)
plt.ylim(-0.15, 0.15)
ax.set_xlabel('X-axis', fontweight ='bold')
ax.set_ylabel('Y-axis', fontweight ='bold')
ax.set_zlabel('Z-axis', fontweight ='bold')
ax.set_title('End effector Trajectory', fontsize = 16, fontweight ='bold')

#running loop for different iterations of time

for i in points:
    time=i
    #print(i)
    y_dot=(radius)*cos(omega*time)*omega#Vy
    z_dot=-(radius)*sin(omega*time)*omega#Vz
    x_dot=0#Vx
    X_dot=Matrix([[x_dot],[y_dot],[z_dot],[0],[0],[0]])#q_dot
    jacobian_matrix_1=jacobian_matrix.subs([(theta_1,q[0]),(theta_2,q[1]),(theta_3,q[2]),(theta_4,q[3]),(theta_5,q[4]),(theta_6,q[5])]).evalf()#jacobian matrix
    jacobian_inverse= jacobian_matrix_1.inv()
    q_dot=jacobian_inverse*X_dot#finding q_dot
    del_time=200/50
    q= (q + q_dot*del_time)#formula for finding q
    ans_6=ans_6.subs([(d1, 0.333),(d3, 0.3160),(d5,0.3840),(d7,0.2070),(a3,0.088)]).evalf()#substituing values of a and d in T0->6
    x_coord,y_coord,z_coord=get_coordinates(q,x_coord,y_coord,z_coord,ans_6,z) #calculating goal postion of end effector 
    torque=g_q.subs([(theta_1,q[0]),(theta_2,q[1]),(theta_3,q[2]),(theta_4,q[3]),(theta_5,q[4]),(theta_6,q[5])]).evalf()- jacobian_matrix_1.T*force #Calculating Torque
    torque_values.append(torque) #making list of values
    z=z+1
    ax.scatter(x_coord, y_coord, z_coord)
    plt.pause(0.5)
    

#plotting Joint Torque graphs

fig,ax_1=plt.subplots(2,3)
torque_values=np.array(torque_values)
ax_1[0,0].scatter(points,torque_values[:,0],s=3)
ax_1[0,0].set_title("Joint 1 Torque")
ax_1[0,1].scatter(points,torque_values[:,1],s=3)
ax_1[0,1].set_title("Joint 2 Torque")
ax_1[0,2].scatter(points,torque_values[:,2],s=3)
ax_1[0,2].set_title("Joint 4 Torque")
ax_1[1,0].scatter(points,torque_values[:,3],s=3)
ax_1[1,0].set_title("Joint 5 Torque")
ax_1[1,1].scatter(points,torque_values[:,4],s=3)
ax_1[1,1].set_title("Joint 6 Torque")
ax_1[1,2].scatter(points,torque_values[:,5],s=3)
ax_1[1,2].set_title("End Effector Joint Torque")

plt.show()