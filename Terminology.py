import enum
import imp
from tracemalloc import start
from turtle import fillcolor
from cv2 import circle
from manim import *
from random import randint, randrange, seed, uniform
from random import random

from numpy import ndarray

#definitions/////////////////////////////

#DAG: 
class CreateDAG(Scene):
    def construct(self):
        dots = [[-1,-1,0], [1,0,0], [3,-0.5,0], [3,2,0], [3,0,0], [5,-0.5,0], [5,2,0]]
        for i,coor in enumerate(dots):
            dot = Dot(coor)
            circle = Circle(radius=0.2, color=WHITE).move_to(dot)
            if(i > 1):
                edge = Arrow(start=dot, end=dots[i-2])
                self.play(edge)
            self.play(Create(circle))


        """
        circles = [[]]
        circles_list = []
        seed(10)
        # adding genesis:
        dot = Dot([-6, uniform(-2, 2), 0])
        circle = Circle(radius=0.5, color=WHITE).move_to(dot)
        circles_list.append(circle)  # create a circle
        genesis = Text("Genesis", height=1)
        genesis.move_to(dot)
        self.play(Create(circle))  # show the circle on screen
        self.play(Create(genesis))
        circles.append(circles_list)
        for i in range(-2, 2):
            for j in range(randint(0,5)):
                dot = Dot([i, uniform(-2, 2), 0])
                circle = Circle(radius=0.2, color=WHITE).move_to(dot)
                circles_list.append(circle)  # create a circle
                self.play(Create(circle))  # show the circle on screen
            circles.append(circles_list)
        
        for i, column in enumerate(circles):
            if(i == 0):
                continue
            for block in column:
                arrow = Arrow(start=block, end=circles[i-1][])"""
