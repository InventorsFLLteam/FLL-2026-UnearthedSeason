######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *

######################## Route parallel program ########################
def Route1():
    MoveStraight_Distance(400,500,490,True,True,Stop.BRAKE)
    rightArm.run_time(-300, 620, then=Stop.BRAKE, wait=True)
    wait(300)
    rightArm.run_time(300, 620, then=Stop.BRAKE, wait=True)
    wait(300)
    rightArm.run_time(-300, 620, then=Stop.BRAKE, wait=True)
    wait(300)
    rightArm.run_time(300, 620, then=Stop.BRAKE, wait=True)
    wait(300)
    rightArm.run_time(-300, 620, then=Stop.BRAKE, wait=True)
    wait(300)
    rightArm.run_time(300, 620, then=Stop.BRAKE, wait=True)
    wait(300)
    rightArm.run_time(-300, 620, then=Stop.BRAKE, wait=True)
    wait(300)
    rightArm.run_time(300, 620, then=Stop.BRAKE, wait=True)
    PointTurn_Angle(300, 300, -90, True, Stop.BRAKE)
    MoveStraight_Distance(400,400,40,True,True,Stop.BRAKE)
    PointTurn_Angle(300, 300, 90, True, Stop.BRAKE)
    rightArm.run_time(-450, 430, then=Stop.BRAKE, wait=True) 
    MoveStraight_Distance(200,200,270,True,True,Stop.BRAKE)#ευθεια προς Σιδηρουργείο
    PointTurn_Angle(300, 300, -20, True, Stop.BRAKE)
    rightArm.run_time(-450, 155, then=Stop.BRAKE, wait=True) 
    PointTurn_Angle(300, 300, -20 ,True, Stop.BRAKE)
    MoveStraight_Distance(200,200,30,True,True,Stop.BRAKE)
    PointTurn_Angle(300, 300, -22 ,True, Stop.BRAKE)
    MoveStraight_Distance(200,200,-47,True,True,Stop.BRAKE)
    rightArm.run_time(450, 600, then=Stop.BRAKE, wait=True) 
    PointTurn_Angle(300, 300, 145 ,True, Stop.BRAKE)
    MoveStraight_Distance(200,200,350,True,True,Stop.BRAKE)
    PointTurn_Angle(300, 300, -85 ,True, Stop.BRAKE)
    MoveStraight_Distance(200,200,120,True,True,Stop.BRAKE)
    leftArm.run_time(300,800 , then=Stop.BRAKE, wait=True)
    MoveStraight_Distance(200,200,-20,True,True,Stop.BRAKE)
    PointTurn_Angle(300, 300, -33 ,True, Stop.BRAKE)
    leftArm.run_time(-100,900 , then=Stop.BRAKE, wait=True)
    MoveStraight_Distance(200,200,-130,True,True,Stop.BRAKE)
    PointTurn_Angle(300, 300, 40 ,True, Stop.BRAKE)
    MoveStraight_Distance(200,200,30,True,True,Stop.BRAKE)
