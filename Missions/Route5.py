######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *

  
######################## Route program ########################
def Route5():
    leftArm.run_time(500, 3000, then=Stop.BRAKE, wait=False) 
    rightArm.run_time(500, 3000, then=Stop.BRAKE, wait=True) 
