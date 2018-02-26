# BraveBots FRC Computer Vision
Computer Vision used during the FRC 2018 competition.


![alt text](https://upload.wikimedia.org/wikipedia/en/thumb/7/7f/Blanchetlogo.png/200px-Blanchetlogo.png)

# Running the Files


Clone the Repository and Enter the following command in the Terminal

```bash

python3 <insert file name here>

```
# Summary

Detect Cube uses contour calculations and color detection to determine whether or not the robot is looking at a cube.

Detect Scale uses contour calculation, color detection, and the hough circles algorithm to determine if the scale is in view.

Detect Color uses the Adafruit color sensor to calculate lumosity of the floor and determines if it is in a specific area of the field.

All of these programs uses the Network Tables API to communicate with the robot.



