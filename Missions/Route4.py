######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *

  
######################## Route program ########################
def Route4():
    
    ###################### Mission 12 ######################
    rightArm.run_time(1000, 500, then=Stop.BRAKE, wait=False)
    MoveStraight_Distance(400,250,401,True,True,Stop.BRAKE)
    rightArm.run_time(-130, 500, then=Stop.BRAKE, wait=False)
    wait(300)
    MoveStraight_Distance(400,250,-250,True,True,Stop.BRAKE)
    PointTurn_Angle(300, 300, -45, True, Stop.BRAKE)
    MoveStraight_Distance(400,250,220,True,True,Stop.BRAKE)
    PointTurn_Angle(300, 300, 42, True, Stop.BRAKE)
    MoveStraight_Distance(400,250,173,True,True,Stop.BRAKE)
    MoveStraight_Distance(400,250,-210,True,True,Stop.BRAKE)
    
    # # # ###################### Mission 15 ######################
    PointTurn_Angle(300, 300, -182, True, Stop.BRAKE)
    MoveStraight_Distance(400,250,-370,True,True,Stop.BRAKE)
    leftArm.run_time(-1000, 550, then=Stop.BRAKE, wait=False)
    wait(1000)
    
    ###################### Mission 01 ######################
    MoveStraight_Distance(400,400,660,True,True,Stop.BRAKE)
    # ###################### Επανατοποθέτηση Ρομπότ ######################
    wait(3500)
    ###################### Συνέχεια της Αποστολής ######################
    leftArm.run_time(150, 1000, then=Stop.BRAKE, wait=False)
    MoveStraight_Distance(700,700,650,True,True,Stop.BRAKE)
    MoveStraight_Distance(850,700,-170,True,True,Stop.BRAKE)
    MoveStraight_Distance(450,400,170,True,True,Stop.BRAKE)
    leftArm.run_time(-300, 1000, then=Stop.BRAKE, wait=False)
    MoveStraight_Distance(100,300,-150,True,True,Stop.BRAKE)
    leftArm.run_time(300, 1000, then=Stop.BRAKE, wait=True)
    MoveStraight_Distance(500,400,-480,True,True,Stop.BRAKE)
