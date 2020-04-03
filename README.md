# ENPM661 Project 3 Phase 3 and 4

## Introduction

The goal of this project is to find the optimal path through a Cartesian maze with obstacles for a rigid robot using the A* algorithm. The robot for this project is the Turtlebot, a two wheeled differential drive robot. It has 8 possible movements, defined by a combination of 3 speeds for the left and right wheels (user defined Fast, Slow, and 0). The default maze is 10200x10200 with 8 obstacles - 4 circles, 3 squares, and a hollow rectangle at the border.

![maze](https://github.com/BrianBock/ENPM661-Project3-Phase3-4/blob/master/Images/maze.png)

The user specifies a start point and goal point in the maze and the program finds the optimal path to the goal.

## Instructions for Running the Program

To run the program, clone this repository. Open a new terminal window and navigate to the repoistory directory. Type `python Astar_rigid.py`, if you have additional older versions of python installed you may need to run `python3` instead. The program will prompt you to enter a start point and goal point, the radius of your robot, and the clearance between your robot and the obstacles. If the points are valid and a solution is possible, the program will then show the visualization of the solution. This mode treats your robot as a circle with the given radius and expands all of the obstacles by the radius and clearance.

In our tests, the program usually solves the path in less than 3 seconds, but takes up to 35 minutes to export the visualization/video. 


## Output

The program has two toggles at the top of the of the `Astar_rigid.py` file. If `write_to_video` is set to `True`, the program will output a video of the solution, including all searched nodes. If `show_visualization` is set to `True`, the program will show the visualization as it is being created. 

The visualization first shows all of the searched nodes. For each node in the list of searched nodes any of the viable neighbors of that node are plotted as arrows. The current arrow is show in cyan. After a searched node is within the goal, the program uses backtracking to find the optimal course which is plotted with red arrows. 

![visualization](https://github.com/jaybrecht/ENPM661-Project3/blob/master/Images/visualization.gif)


## Creating New Mazes

The maze is generated by reading in a text file. New mazes can be generated by creating new text files that follow the same format. 

The first parameters needed to establish a maze is the height and width of the maze in points. This can be specified by the lines. **Note it is crucial to use a colon** `:`

    height: XX
    width: XX

The code currently supports four different types of obstacles; circles, ellipses, polygons, and rotated rectangles. Depending on the type of obstacle you want to generate, different parameters are needed. All coordinates are in Cartesian coordinates, with the origin at the bottom left corner of the maze.  

### Circle
For a circle the file needs to contain a center point (x,y) and a radius (r). The lines in text file should look like this

    circle
        center: x,y
        radius: r

### Ellipse
To add a rotated rectangle obstacle you need to specify the center point (x,y), the major and minor axis (a1,a2), the rotation angle in degrees, and the start and end angles in degrees. To specify the entire ellipse the start should be 0 and the end 360. The lines in text file should look like this

    ellipse
        center: x,y
        axis: a1,a2
        angle: a 
        start: a
        end: a
        

### Polygon
To add a polygon obstacle you need to specify all points that make up the exterior of the polygon in the form (x,y). The program will draw lines between each point so the order matters - they must be defined clockwise. It does not matter which point you start from. The lines in text file should look like this

    polygon
        point: x1,y1
        point: x2,y2
        point: x3,y3
        point: x4,y4

### Rotated Rectangle
To add a rotated rectangle obstacle you need to specify the position of the starting corner (the code currently only supports the starting corner as the bottom right corner), the length of both sides l1 and l2, and the rotation angle. The lines in text file should look like this

    rotatedrect
        start_point: x,y
        l1: l1
        l2: l2
        angle: a

### Aditional Properties
Each obstacles can also have a specified color and alpha. To specify these properties, add color and alpha lines under the given obstacle. The color can be any of the colors from the [XKCD color survey](https://xkcd.com/color/rgb/). The alpha should be a number between 0 and 1. The closer to 0, the more transparent the obstacle will appear. 

    obstacle
        color: xkcd_color
        alpha: 0-1

## Dependencies 

    cv2
    numpy
    matplotlib
    datetime
    
