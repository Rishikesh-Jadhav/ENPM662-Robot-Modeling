# ENPM662-Robot-Modeling
This repository serves as a comprehensive record of my academic journey in ENPM662 during the Fall of 2022. It encompasses solutions and code submissions for all projects, providing dedicated folders for each project, along with accompanying documentation and resources.

## 📚 Course Overview
The Robot Modeling course provides a foundational understanding of robot modeling principles, covering forward and inverse kinematics, velocity kinematics, Jacobians, dynamics, planning, and contact. While the primary focus is on serial open-chain robots, the curriculum also touches on parallel robots, closed-chain systems, aerial and mobile robots, hyper-redundant systems, and grasping.

## 📄 Assignemnet List

### [Assignemnet 1](https://github.com/Rishikesh-Jadhav/ENPM662-Robot-Modeling/tree/main/Assignment1): Kinematics
- **Objectives**:
    - Python program to plot the 2D trajectory of a rear-wheel drive vehicle.
    - Deriving the kinematics equations for a 3-DOF manipulator using the geometrical method.

### [Assignemnet 2](https://github.com/Rishikesh-Jadhav/ENPM662-Robot-Modeling/tree/main/Assignment2): Robot Modeling and Homogeneous Transformations
- **Objectives**:
    - Composing homogeneous transformation matrices based on rotations and translations.
    - Exploring methods for expressing the coverage area of a camera mounted on a drone, considering consecutive rotations and 3D locations
    -  Deriving transformation matrix between two frames, particularly considering rotations and translations
    -  Applying concepts of kinematics to plan and optimize trajectories for a drone, considering positional changes and rotations to achieve a desired final orientation.
      
### [Assignemnet 3](https://github.com/Rishikesh-Jadhav/ENPM662-Robot-Modeling/tree/main/Assignment3): Robot position Kinematics on Panda and KUKA LBR iiwa robot
- **Objectives**:
    - Setting up forward position kinematics for the Panda robot using the Denavit-Hartenberg convention.
    - Utilizing Python's SymPy library to establish D-H equations, drawing frames, creating tables, and determining transformation matrices.
    - Implementing forward position kinematics for the KUKA LBR iiwa robot using the Denavit-Hartenberg convention.
    - Assigning frames, creating the D-H table, and delivering necessary documentation without requiring homogeneous transformation matrices or geometric validation.
      
### [Assignemnet 4](https://github.com/Rishikesh-Jadhav/ENPM662-Robot-Modeling/tree/main/Assignment4): Inverse Kinematics and Trajectory Generation for Panda Robot
- **Objectives**:
    - Applying the inverse velocity kinematics (Inverse Jacobian) for the Franka Emika Panda robot.
    - Generating a 10 cm radius circle within 5 seconds using inverse velocity kinematics.
    - Seting up the Jacobian matrix for the robot via discussed methods in class.
    - Deriving the circular trajectory equation, obtaining joint angular velocities, performing numerical integration for joint angles, and visualizing the circular trajectory using forward position kinematics.
    
### [Assignemnet 5](https://github.com/Rishikesh-Jadhav/ENPM662-Robot-Modeling/tree/main/Assignment5): Manipulator Dynamics - Joint Torque Computation for Panda Robot
- **Objectives**:
    - Calculating the joint torques required for the Panda robot to compensate for its weight and exert a 5 N force against the wall while drawing a circle of radius 10 cm within 200 seconds
    - Setting up the Jacobian and Transformation matrices, Utilizing inbuilt functions for Gravity Matrix setup, considering derivatives, cross-products, and matrix inversion and applying Lagrange's equation to compute joint torques, incorporating kinetic and potential energy considerations. 

## 📚 Required Resources
- **Textbook:** [Robot Modeling and Control](link_to_resource) by Mark W. Spong, Seth Hutchinson, and M. Vidyasagar.
- **Textbook:** [Planning Algorithms](http://planning.cs.uiuc.edu/) by Steven LaValle, Cambridge University Press, 2006.


