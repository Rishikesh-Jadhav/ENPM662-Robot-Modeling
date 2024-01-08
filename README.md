# ENPM662-Robot-Modeling
This repository serves as a comprehensive record of my academic journey in ENPM662 during the Fall of 2022. It encompasses solutions and code submissions for all projects, providing dedicated folders for each project, along with accompanying documentation and resources.

## 📚 Course Overview
The Robot Modeling course explores planning techniques essential for realizing autonomous robots. Covering task planning, motion planning, and trajectory planning, the curriculum emphasizes traditional motion planning techniques with a focus on integrating physics into the planning process. Mobile robots are used as examples throughout the course, and the techniques introduced are equally applicable to robot manipulators.

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


## 📚 References
- **Textbook:** [Planning Algorithms](http://planning.cs.uiuc.edu/) by Steven LaValle, Cambridge University Press, 2006.
- **Mobile Robotics: Mathematics, Models, and Methods** by Alonzo Kelly, Cambridge University Press, 2013.
- **Principles of Robot Motion: Theory, Algorithms, and Implementations** by Howie Choset et al., MIT Press, 2005.
- **Probabilistic Robotics
