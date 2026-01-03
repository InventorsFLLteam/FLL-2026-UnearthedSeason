######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *

  
######################## Route program ########################
def Route6():
  MoveStraight_Distance(400,400,290,True,True,Stop.BRAKE)
  PointTurn_Angle(300, 300, 90, True, Stop.BRAKE)
  MoveStraight_Distance(400,400,750,True,True,Stop.BRAKE)
  PointTurn_Angle(300, 300, -90, True, Stop.BRAKE)
  MoveStraight_Distance(400,400,500,True,True,Stop.BRAKE)
  PointTurn_Angle(300, 300, 48, True, Stop.BRAKE)
  MoveStraight_Distance(400,400,110,True,True,Stop.BRAKE)
  leftArm.run_time(-50, 600, then=Stop.BRAKE, wait=True)
  leftArm.run_time(-300, 600, then=Stop.BRAKE, wait=True)
  MoveStraight_Distance(400,400,-100,True,True,Stop.BRAKE)
  PointTurn_Angle(300, 300, -150, True, Stop.BRAKE)
  MoveStraight_Distance(400,400,420,True,True,Stop.BRAKE)
  rightArm.run_time(50,600 , then=Stop.BRAKE, wait=True)
  rightArm.run_time(300,600 , then=Stop.BRAKE, wait=True)
  MoveStraight_Distance(400,400,-70,True,True,Stop.BRAKE)
  PointTurn_Angle(300, 300, 100, True, Stop.BRAKE) 
  MoveStraight_Distance(400,400,-240,True,True,Stop.BRAKE) 
