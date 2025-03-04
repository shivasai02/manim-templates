# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla

from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class C2Anim(AbstractAnim):
    
    def construct(self):
        #  p1=cvo.CVO().CreateCVO("cname","oname")
        p10=cvo.CVO().CreateCVO("Person","John Doe")
         
        p11 = cvo.CVO().CreateCVO("Previous Employer","Google")
        p10.cvolist.append(p11)
               
        self.setNumberOfClasses(2)
         
        self.positionChoice = [[-4,-2,0],[4,2,0]]
        self.angleChoice = [TAU/4]
        self.colorChoice=[ORANGE,YELLOW]
        self.isRandom = False
        self.construct1(p10,p10)
  
            
if __name__ == "__main__":
    scene = C2Anim()
    scene.render()