######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *

######################## Route parallel program ########################

# Example action
# def __Route1_LeftArm1(duration):
    # leftArm.run(500)
    # wait(1000)
    # leftArm.brake()
    
######################## Route program ########################

### Starting position ###
# Blue base - Align left wheel left side to 2nd Bold line from left

def Route1():
    # """ Start your code here """
    # Step 1 - Move forward
    
    ####### παράδειγμα από MoveStraigh_Distance #########
    # speed, accel, distance, useGyro, waitForComplete, stopMethod #
    # MoveStraight_Distance(400,400,1000,True,True,Stop.BRAKE)
    
    ####### παράδειγμα από MoveSteering_Seconds #########
    # speed, steering, duration #
    # MoveSteering_Seconds(400, 0, 2000)

    ######## παράδειγμα από PointTurn_Angle #######
    # speed, accel, angle #
    # PointTurn_Angle(300, 300, 90, False, Stop.BRAKE)
    
    ######## παράδειγμα από rightArm.run_time #######
    # speed, time seconds, stopMethod, waitForComplete #
    rightArm.run_time(500, 3000, then=Stop.BRAKE, wait=True) 