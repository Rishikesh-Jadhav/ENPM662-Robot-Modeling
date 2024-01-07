This folder is created by Rishikesh Jadhav(UID:119256534) for ENPM 662 Project-1

This folder consists of 4 sub folders:

	Assembly:Contains the zip folder of the assembly which contains the part models and the 		 	 assembly files.
	Package: Contains the zip folder of the package. Package includes the following sub 		                 folders:-
			a.config
			b.launch
			c.meshes
			d.src
			e.textures
			f.urdf
			d.World
			and other files:-(publisher.py,subscriber.py)
	Report:  Report of project_1 in pdf format
	Results: Provided simulation videos just in case the video link in the report doesn't 			 	 work.

Instructions to run the package:

1.Unzip the package(updated_assembly).

2.Move the folder into the src folder of the catkin workspace of your system. 

3.Build the package by using the command - catkin_make clean && catkin_make (Don’t  forget  to     source before you build your package). 

4.Launch the car in Gazebo using the command - roslaunch updated_assembly             updated_assembly.launch.

5.In a parallel terminal open rviz to visualize the robot.(don't forget to start simulation in     gazebo before visualizing in Rviz.)

6.In another terminal open the teleop file using the command- python3 teleop_template.py.
  to control the car in Gazebo.
 
7.The above instructions will help you move the robot manually in Gazebo and visualize in Rviz.
 
8.Now to run the publisher_subscriber, open 4 terminals(1 for roscore,1 for lauching the robot     in Gazebo ,1 for publisher,1 for subscriber ) 

9.Note that to run the publisher and subscriber file to make the robot go round in a circle in     an empty world, comment out the competion arena line in the launch file.  

10.After completing the steps above in the given order, the car should go round in circles in     the empty world in Gazebo.